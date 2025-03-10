# Class05 Code Examples

## IMU sensor 

Setting up for IMU
``` #import package IMU sensor need
import os, sys, io
import M5
from M5 import *
from hardware import I2C
from hardware import Pin
from unit import IMUProUnit
```
configure IMU on I2C port, in this example we connect IMU to port 1 and 2. Change pins if the connection changed. 
```
# configure I2C port on pins 1 and 2:
i2c = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
# configure IMU on I2C port:
imu = IMUProUnit(i2c)
```
