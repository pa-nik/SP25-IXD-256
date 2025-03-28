# MQTT button publish to Adafruit IO feed

import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import network
from umqtt import *

ssid = 'INSERT_WIFI_NAME'
password = 'INSERT_WIFI_PASSWORD'

aio_user_name = 'INSERT_ADAFRUIT_IO_USERNAME'
aio_password = 'INSERT_ADAFRUIT_IO_PASSWORD'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print('connect to WiFi...')
while wifi.isconnected() == False:
    print('.', end='')
    time.sleep_ms(100)

print('WiFi connection successful')
ip_list = wifi.ifconfig()
ip_address = ip_list[0]
print('IP address:', ip_address)

mqtt_client = MQTTClient(
  'testclient-' + aio_user_name,
  'io.adafruit.com',
  port = 1883,
  user = aio_user_name,
  password = aio_password,
  keepalive = 3000
)
# connect to MQTT broker:
mqtt_client.connect(clean_session=True)  

M5.begin()

# initialize built-in RGB light on AtomS3 Lite:
rgb = RGB()

# callback function to run when data is received:
def feed_callback(data):
    # print the received data (feed name followed by value)
    #print('received..', data)
    # print the decoded value of received data:
    data_val = data[1].decode()
    print('received..', data_val)
    # turn on RGB LED green or red based data value:
    if (data_val == '1'):
        rgb.fill_color(0x00ff00)  # fill with green
    elif (data_val == '0'):
        rgb.fill_color(0xff0000)  # fill with red
    
    
# subscribe to button-feed and run feed_callback function
# when data is received:
mqtt_client.subscribe(aio_user_name+'/feeds/button-feed', feed_callback)
    

while True:
  M5.update()
  
  if BtnA.wasPressed():
    print('button pressed..')
    mqtt_client.publish(aio_user_name+'/feeds/button-feed', '1', qos=0)
  elif BtnA.wasReleased():
    print('button released..')
    mqtt_client.publish(aio_user_name+'/feeds/button-feed', '0', qos=0)

  # check for messages on subscribed feeds:
  mqtt_client.check_msg()
  
  time.sleep_ms(100)  
  
