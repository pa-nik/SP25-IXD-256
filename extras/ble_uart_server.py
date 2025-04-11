# BLE UART server example for M5Stack AtomS3
# run the BLE UART client example on another AtomS3 board

import os, sys, io
import M5
from M5 import *
from bleuart import *
import time

M5.begin()
ble_server = BLEUARTServer(name='ble-uart')

while True:
    M5.update()
    print('write to client..')
    ble_server.write('hello M5!')
    time.sleep_ms(2000)
  
