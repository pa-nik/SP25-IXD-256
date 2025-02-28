from machine import Pin
from time import *
from neopixel import NeoPixel

# configure pin 41 as input
# (built-in button on AtomS3 Lite)
btn = Pin(41, Pin.IN)

# configure NeoPixel object on pin 35 for 1 pixel:
# (built-in RGB LED on AtomS3 Lite)
np = NeoPixel(Pin(35), 1)

while True:
    #print('btn =', btn.value())
    if btn.value():
        print('a')
        # set neopixel to black:
        np[0] = (0, 0, 0)  
    else:
        print('b')
        # set neopixel to green:
        np[0] = (0, 255, 0)
    # display neopixel color:
    np.write()  
    sleep_ms(100)

