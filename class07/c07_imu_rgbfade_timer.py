import os, sys, io
import M5
from M5 import *
from hardware import I2C
from hardware import Pin, ADC
from unit import IMUProUnit
from time import *
from neopixel import NeoPixel
import m5utils  # remap function

# initialize M5 hardware:
M5.begin()

# configure I2C port on pins 1 and 2:
i2c = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)

# configure IMU on I2C port:
imu = IMUProUnit(i2c)

# configure NeoPixel object on pin 35 for 1 pixel:
# (built-in RGB LED on AtomS3 Lite)
#np = NeoPixel(Pin(35), 1)

# configure NeoPixel on pin7 for 30 pixels:
# (black connector on PortABC plugged into AtomS3 Lite)
np = NeoPixel(Pin(7), 30)

# configure ADC on pin 6:
# (blue connector on PortABC plugged into AtomS3 Lite)
adc = ADC(Pin(6))

# configure the ADC sensitivity:
adc.atten(ADC.ATTN_11DB)

# variables for previous (last) x, y-axis acceleration:
imu_x_last = 0
imu_y_last = 0

# variables for current r, g, b colors:
r = 0
g = 0
b = 0
# variables for final r, g, b colors:
r_final = 0
g_final = 0
b_final = 0

# variable for imu timing:
imu_timer = 0

# variable for ADC timing:
adc_timer = 0

while True:
    # update M5 hardware:
    M5.update()
    
    # read ADC and print values every 200ms (5 times per sec)
    if (ticks_ms() > adc_timer + 200):
        # update adc timer to current time:
        adc_timer = ticks_ms()
        # read the ADC value:
        angle_val = adc.read()
        # remap angle_val from 0 - 4095 range to 0 - 255 range:
        brightness = int(m5utils.remap(angle_val, 0, 4095, 0, 100))
        #print('brightness =', brightness)
    
    # read imu and print values every 100ms (10 times per sec)
    if (ticks_ms() > imu_timer + 100):
        # update imu timer to current time:
        imu_timer = ticks_ms()
        
        # read accelerometer values from IMU:
        imu_val = imu.get_accelerometer()
    
        # print all (x, y, z) accelerometer values:
        #print(imu_val)
        
        # print the X-axis accelerometer value:
        #print(imu_val[0])  # value at index 0
        
        # variables for x, y-axis acceleration:
        imu_x = imu_val[0]
        imu_y = imu_val[1]
        
        # print imu_x, imu_y values:
        #print(imu_x, imu_y)
        # print imu_x value for ProtoPie (message||value format):
        #print('imu_x||' + str(imu_x))
        # remap imu_x value from -1.0 - 1.0 range to 0 - 300 range:
        imu_x_protopie = int(m5utils.remap(imu_x, -1.0, 1.0, 0, 300))
        # print imu_x_protopie value for ProtoPie (message||value format):
        print('imu_x||' + str(imu_x_protopie))
    
        # x-axis tilt conditions:
        if (imu_x > 0.5) or (imu_x < -0.5):
            #print('X tilt')
            r_final = 255
            g_final = 0
            # print 'b' for ProtoPie:
            print('b')
        # y-axis tilt conditions:
        elif (imu_y > 0.5) or (imu_y < -0.5):
            #print('Y tilt')
            r_final = 0
            g_final = 255
            # print 'b' for ProtoPie:
            print('b')
        else:
            #print('no tilt')
            r_final = 0
            g_final = 0
            # print 'a' for ProtoPie:
            print('a')

        # x-axis motion conditions:
        if (imu_x - imu_x_last > 0.5) or \
           (imu_x - imu_x_last < -0.5):
            b_final = 255
        else:
            b_final = 0
            
        # update imu_x_Last value:
        imu_x_last = imu_x
        
        # print the Y-axis accelerometer value:
        #print('y =', imu_val[1])  # value at index 1
        
        # print the X and Y accelerometer values:
        #print(imu_val[0], imu_val[1])
        
    # increment r, g, b towards final values:
    if (r < r_final):
        r += 1
    elif (r > r_final):
        r -= 1
    if (g < g_final):
        g += 1
    elif (g > g_final):
        g -= 1
    if (b < b_final):
        b += 1
    elif (b > b_final):
        b -= 1
        
    # set color for 30 pixels:
    red = int(r * brightness/100)
    green = int(g * brightness/100)
    blue = int(b * brightness/100)
    for i in range(30):
        # set neopixel to red, green, blue values
        np[i] = (red, green, blue)  
    np.write()  # display neopixel color
    
    sleep_ms(10)
    
