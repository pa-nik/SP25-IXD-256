Class 04 Code Examples
```python
# configure ADC on pin 1:
adc = ADC(Pin(1))
```

```python
# configure ADC on an input pin:
adc = ADC(analog_pin)
```

```python
# configure the ADC sensitivity:
adc.atten(ADC.ATTN_11DB)
```

```python
# print(analog_val)
analog_val_8bit = int(analog_val/16)
print(analog_val_8bit)
```

displaying a link with Markdown syntax:  
[link to ADC read example](c04_adc_read.py)  

displaying a link with HTML syntax:  
<a href="c04_adc_read.py">link to ADC read example</a>  
  
displaying an image with Markdown syntax:  
![image description](../assignment03/a03_splash.jpg)
  
displaying an image with set width using HTML syntax:  
<img src="../assignment03/a03_splash.jpg" width="500">


