# SP25-IXD-256
Code examples and templates for IXD-256: Advanced Interactive Prototyping.   
  
### Resources / Links  
[AtomS3 Lite Documentation](https://docs.m5stack.com/en/core/AtomS3%20Lite)  
[MicroPython ESP32 Reference](https://docs.micropython.org/en/latest/esp32/quickref.html)  
[Code for the book *Programming the ESP32*](https://github.com/simonmonk/prog_esp32/tree/main/esp32_lite)  
[Thonny - Python IDE for Microprocessors](https://thonny.org/)  
[Editing Files on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)  
[GitHub Markdown Tutorial](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)  
  
### MicroPython ESP32 Reference Links
[Pulse Width Modulation (PWM)](https://docs.micropython.org/en/latest/esp32/quickref.html#pwm-pulse-width-modulation)  
[Analog to Digital Converter (ADC)](https://docs.micropython.org/en/latest/esp32/quickref.html#ADC)  
[NeoPixel RGB LEDs](https://docs.micropython.org/en/latest/esp32/quickref.html#neopixel-and-apa106-driver)  

### M5Stack Reference Links  
[IMU Pro Unit](https://uiflow-micropython.readthedocs.io/en/latest/units/imupro.html)  
  
### Class Examples  
[c04_adc_read.py](class04/c04_adc_read.py) - ADC read example  
[c04_adc_read_to_neopixel.py](class04/c04_adc_read_to_neopixel.py) - ADC read to NeoPixel color  
[c05_imu_read.py](class05/c05_imu_read.py) - IMU Pro read example  
[c06_imu_tilt_and_motion.py](class06/c06_imu_tilt_and_motion.py) - IMU Pro tilt and motion example  
[c06_btn_print_ab.py](class06/c06_btn_print_ab.py) - print `'a'` or `'b'` for button press/release for ProtoPie  
[c06_adc_print_angle.py](class06/c06_adc_print_angle.py) - print ADC `message||value` for ProtoPie  
[c07_imu_rgbfade_timer.py](class07/c07_imu_rgbfade_timer.py) - fade RGB LEDs without using delay, use of `ticks_ms()`  
[c08_pwm_input.py](class08/c08_pwm_input.py) - control servo with PWM using `input` function  
