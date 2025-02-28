from machine import Pin, ADC
from time import *
from neopixel import NeoPixel

# configure pin 41 as input
# (built-in button on AtomS3 Lite)
btn = Pin(41, Pin.IN)

# configure NeoPixel object on pin 35 for 1 pixel:
# (built-in RGB LED on AtomS3 Lite)
np = NeoPixel(Pin(35), 1)

# configure pin 1 as input:
analog_pin = Pin(1, Pin.IN)

# configure ADC on an input pin:
adc = ADC(analog_pin)

# configure the ADC sensitivity:
adc.atten(ADC.ATTN_11DB)

while True:
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
    # read the ADC value:
    analog_val = adc.read()
    # print message||value for ProtoPie:
    print('angle||' + str(analog_val))
    sleep_ms(100)

