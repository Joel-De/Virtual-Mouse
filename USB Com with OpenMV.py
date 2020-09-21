import sensor, image, time, math
import pyb, ustruct, USB_VCP

threshold_index = 0

thresholds = [(  0, 100,   -9,  -64, -128,  127), 
              (30, 100, -64, -8, -32, 32),
              (0, 30, 0, 64, -128, 0)] 
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking

sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.RGB565)
sensor.skip_frames(time = 2000)

usb = USB_VCP()
clock = time.clock()

bus = pyb.I2C(2, pyb.I2C.SLAVE, addr=0x12)
bus.deinit() # Fully reset I2C device...
bus = pyb.I2C(2, pyb.I2C.SLAVE, addr=0x12)

while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs([thresholds[threshold_index]], pixels_threshold=50, area_threshold=50, merge=True):
            # These values depend on the blob not being circular - otherwise they will be shaky.
            if blob.roundness() > 0.8:
                img.draw_edges(blob.min_corners(), color=(255,0,0))
                img.draw_line(blob.major_axis_line(), color=(0,255,0))
                img.draw_line(blob.minor_axis_line(), color=(0,0,255))
            # These values are stable all the time.
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
            value = str(blob.cx()) + "\n"
            usb.send(bytes('value', 'ascii'))
