from hardware import *
#from machine import Pin, PWM
from time import *

# configure PWM on pin 2 with 50Hz frequency:
pwm = PWM(Pin(2), freq=50)

# configure PWM frequency at 50Hz for servo:
#pwm.freq(50)

# configure duty cycle to stop the servo:
pwm.duty(75)

# use numbers between 60 - 100 to move servo

while True:
    # move the servo slowly clockwise:
    #pwm.duty(65)
    #sleep_ms(2000)

    # move the servo slowly counter-clockwise:
    #pwm.duty(85)
    #sleep_ms(2000)
    
    duty_cycle = input('type a number between 60 - 100:')
    pwm.duty(int(duty_cycle))

