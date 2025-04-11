# BLE UART client example for M5Stack AtomS3
# run the BLE UART server example on another AtomS3 board

import os, sys, io
import M5
from M5 import *
from bleuart import *
import time

M5.begin()

ble_client = BLEUARTClient()
ble_client.connect('ble-uart', timeout=2000)
print('connected =', ble_client.is_connected())
    
while True:
    M5.update()
    data = ble_client.read()
    if(data != ''):
        print('data =', data.decode())
    time.sleep_ms(100)
  
