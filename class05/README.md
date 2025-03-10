# Class05 Code Examples

## IMU sensor 

Setting up for IMU - Make sure include all before each IMU project
``` #import package IMU sensor need
import os, sys, io
import M5
from M5 import *
from hardware import I2C
from hardware import Pin
from unit import IMUProUnit
from time import * #include this line if have sleep_ms or any time related function 
```

Configure IMU on I2C port, in this example we connect IMU to port 1 and 2. Change pins if the connection changed. 
```
# configure I2C port on pins 1 and 2:
i2c = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
# configure IMU on I2C port:
imu = IMUProUnit(i2c)
```

Read & Print IMU value
```
# read accelerometer values from IMU:
imu_val = imu.get_accelerometer()
# print all (x, y, z) accelerometer values:
print(imu_val)

#--- Use code below to control which axis printing
# print the X-axis accelerometer value:
#print(imu_val[0])  # value at index 0
    
# print the Y-axis accelerometer value:
#print('y =', imu_val[1])  # value at index 1
    
# print the X and Y accelerometer values:
#print(imu_val[0], imu_val[1])
```

