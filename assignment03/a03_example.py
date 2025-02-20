from machine import Pin
from neopixel import NeoPixel
from time import *

print('Assignment #3 Example')

# configure digital input on pin 1:
in1 = Pin(1, Pin.IN, Pin.PULL_UP)
in1_val_last = 1

# configure NeoPixel output on pin 7 for 30 pixels:
NUM_PIXELS = 30
np = NeoPixel(Pin(7), NUM_PIXELS)

program_state = 'START'

# get current running time in milliseconds:
timer_ms = ticks_ms()

while True:
    # check that the input changed from high to low:
    if in1.value() == 0:  # input value is low
        if in1_val_last == 1:  # last input value was high
            if program_state == 'WAITING':
                program_state = 'RUN'
                # update the timer variable:
                timer_ms = ticks_ms()
            print('program_state =', program_state)
    # update the last input value:
    in1_val_last = in1.value()
        
    if program_state == 'START':
        # set all pixels to black color:
        for i in range(NUM_PIXELS):
            np[i] = (0, 0, 0)
        np.write()
        sleep(2)  # wait 2 seconds
        # change to RUN state
        program_state = 'WAITING'
    elif program_state == 'WAITING':
        # fade in green color:
        for n in range(255):
            for i in range(NUM_PIXELS):
                np[i] = (0, n, 0)
            sleep_ms(5)
            np.write()
        # fade from green to black:
        for n in range(255):
            for i in range(NUM_PIXELS):
                np[i] = (0, 255 - n, 0)
            sleep_ms(5)
            np.write()
    elif program_state == 'RUN':
        # change to blue color:
        for i in range(NUM_PIXELS):
            np[i] = (0, 0, 255)
        np.write()
        
        # check if current time is 5 seconds after timer value
        if ticks_ms() > timer_ms + 5000:
            program_state = 'FINISH'
            print('program_state =', program_state)
            
    elif program_state == 'FINISH':
        # fade from blue to black:
        for n in range(255):
            for i in range(NUM_PIXELS):
                np[i] = (0, 0, 255 - n)
            sleep_ms(5)
            np.write()
        program_state = 'ALL DONE!'
        
        
        