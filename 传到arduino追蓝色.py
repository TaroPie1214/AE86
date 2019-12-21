import sensor, image, time
from pyb import UART
import json
blue_threshold   = (48,12,-19,33,-49,-14)
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

while(True):
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

