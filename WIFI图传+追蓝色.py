import sensor, image, time, network, usocket, sys
from pyb import UART
import json

SSID='studyGod' # Network SSID
KEY='ljrsb666'  # Network key
HOST =''     # Use first available interface
PORT = 8080  # Arbitrary non-privileged port

blue_threshold = (48,12,-19,33,-49,-14)
sensor.reset() # Initialize the camera sensor.
sensor.set_hmirror(True)
sensor.set_vflip(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10)
sensor.set_auto_whitebal(False)
clock = time.clock()

uart = UART(3, 9600)
def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob.pixels() > max_size:
            max_blob=blob
            max_size = blob.pixels()
    return max_blob

# Init wlan module and connect to network
print("Trying to connect... (may take a while)...")
wlan = network.WINC()
wlan.connect(SSID, key=KEY, security=wlan.WPA_PSK)

# We should have a valid IP now via DHCP
print(wlan.ifconfig())

# Create server socket
s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)

# Bind and listen
s.bind([HOST, PORT])
s.listen(5)

# Set server socket to blocking
s.setblocking(True)

def start_streaming(s):
    print ('Waiting for connections..')
    client, addr = s.accept()
    # set client socket timeout to 2s
    client.settimeout(2.0)
    print ('Connected to ' + addr[0] + ':' + str(addr[1]))

    # Read request from client
    data = client.recv(1024)
    # Should parse client request here

    # Send multipart header
    client.send("HTTP/1.1 200 OK\r\n" \
                "Server: OpenMV\r\n" \
                "Content-Type: multipart/x-mixed-replace;boundary=openmv\r\n" \
                "Cache-Control: no-cache\r\n" \
                "Pragma: no-cache\r\n\r\n")

    # FPS clock
    clock = time.clock()

    # Start streaming images
    # NOTE: Disable IDE preview to increase streaming FPS.
    while (True):
        clock.tick() # Track elapsed milliseconds between snapshots().
        frame = sensor.snapshot()
        cframe = frame.compressed(quality=35)
        header = "\r\n--openmv\r\n" \
                 "Content-Type: image/jpeg\r\n"\
                 "Content-Length:"+str(cframe.size())+"\r\n\r\n"
        client.send(header)
        client.send(cframe)
        print(clock.fps())
        img = sensor.snapshot()

        blobs = img.find_blobs([blue_threshold])
        if blobs:
            max_blob=find_max(blobs)
            img.draw_rectangle(max_blob.rect())
            img.draw_cross(max_blob.cx(), max_blob.cy())
            pcx = max_blob.cx()



            output_str=json.dumps(max_blob.cx())
            uart.write(output_str + '\r\n')
            print(pcx)
        else:
            print('not found!')


while(True):
    try:
        start_streaming(s)
    except OSError as e:
        print("socket error: ", e)
        #sys.print_exception(e)

