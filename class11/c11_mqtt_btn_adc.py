# MQTT button publish to Adafruit IO feed

import os, sys, io
import M5
from M5 import *
from hardware import *
from time import *
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

# configure ADC on pin 1 (bottom port of AtomS3 Lite)
adc = ADC(Pin(1))
# configure the ADC sensitivity:
adc.atten(ADC.ATTN_11DB)

# variable for ADC timing:
adc_timer = 0

# callback function to run when data is received:
def button_feed_callback(data):
    # print the received data (feed name followed by value)
    #print('received..', data)
    # print the decoded value of received data:
    data_val = data[1].decode()
    print('received from button-feed:', data_val)
    # turn on RGB LED green or red based data value:
    if (data_val == '1'):
        rgb.fill_color(0x00ff00)  # fill with green
    elif (data_val == '0'):
        rgb.fill_color(0xff0000)  # fill with red
    
# subscribe to button-feed and run button_feed_callback function
# when data is received:
mqtt_client.subscribe(aio_user_name+'/feeds/button-feed', button_feed_callback)


# callback function to run when data is received:
def adc_feed_callback(data):
    # print the received data (feed name followed by value)
    #print('received..', data)
    # print the decoded value of received data:
    data_val = data[1].decode()
    print('received from adc-feed:', data_val)
    
# subscribe to adc-feed and run adc_feed_callback function
# when data is received:
mqtt_client.subscribe(aio_user_name+'/feeds/adc-feed', adc_feed_callback)
 

while True:
  M5.update()
  
  if BtnA.wasPressed():
    print('button pressed..')
    mqtt_client.publish(aio_user_name+'/feeds/button-feed', '1', qos=0)
  elif BtnA.wasReleased():
    print('button released..')
    mqtt_client.publish(aio_user_name+'/feeds/button-feed', '0', qos=0)
  
  if BtnA.isPressed():
    # publish ADC value to adc-feed every 5 seconds:
    if (ticks_ms() > adc_timer + 5000):
        # update adc timer to current time:
        adc_timer = ticks_ms()
        # read the ADC value:
        angle_val = adc.read()
        print('angle_val =', angle_val)
        mqtt_client.publish(aio_user_name+'/feeds/adc-feed',
                            str(angle_val), qos=0)

  # check for messages on subscribed feeds:
  mqtt_client.check_msg()
  
  sleep_ms(100)  
  

