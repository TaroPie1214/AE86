import sensor, image, time, network, usocket,pyb
from pyb import UART
import json
SSID='studyGod' # Network SSID
KEY='ljrsb666'  # Network key
HOST =''     # Use first available interface
PORT = 8080  # Arbitrary non-privileged port

global socket_node
socket_node = 0

# Init wlan module and connect to network
print("Trying to connect... (may take a while)...")

wlan = network.WINC()
wlan.connect(SSID, key=KEY, security=wlan.WPA_PSK)

# We should have a valid IP now via DHCP
print(wlan.ifconfig())

#创建 socket 连接，连接成功后发送“Hello 01Studio！”给服务器。
client=usocket.socket()
addr=('10.122.226.244',10003) #服务器 IP 和端口
client.connect(addr)
client.send('Hello 01Studio!')

#开启定时器，周期 100ms,重复执行 socket 通信接收任务
def fun(tim):
    global socket_node
    socket_node = 1
    pyb.LED(3).toggle()

tim = pyb.Timer(4,freq=10)
tim.callback(fun)


sensor.reset() # Initialize the camera sensor.
sensor.set_hmirror(True)
sensor.set_vflip(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10)
sensor.set_auto_whitebal(False)
clock = time.clock()
uart = UART(3, 9600)

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

    while (True):
        global socket_node
        if socket_node:
            text=client.recv(128) #单次最多接收 128 字节
            if text == '':
                pass

            else: #打印接收到的信息为字节，可以通过 decode('utf-8')转成字符串
                print(text)
                client.send('I got:'+text.decode('utf-8'))

            socket_node=0


            output_str=json.dumps(text)
            uart.write(text + '\r\n')
            print(text)
        else:
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




while(True):
    try:
        start_streaming(s)
    except OSError as e:
        print("socket error: ", e)
        #sys.print_exception(e)

