from machine import I2C, Pin, freq
from time import sleep
from lib.ssd1306 import SSD1306_I2C

MAX_CLOCK = 136000000 # 200 MHz
MIN_CLOCK = 50000000 # 50 MHz
CLOCK_SPEED = freq()

del freq

def button_hold(button_down):
    if button_pin.value() == False and not button_down:
        for i in range(10):
            if button_pin.value() == False and not button_down:
                pass
            else:
                return "Press"
            sleep(.05)
        return True
    return False
        

i2c = I2C(id=1, scl=Pin(7), sda=Pin(6))

# Menu Variables
line = 1 
highlight = 1
shift = 0
list_length = 0
TOTAL_LINES = 6
line_height = 10

oled = SSD1306_I2C(width=128, height=64, i2c=i2c, addr=i2c.scan()[0])
oled.init_display()

button_pin = Pin(0, Pin.IN, Pin.PULL_UP)
direction_pin = Pin(1, Pin.IN, Pin.PULL_UP)
step_pin  = Pin(2, Pin.IN, Pin.PULL_UP)

previous_value = True
button_down = not button_pin.value()

led1 = Pin(25, Pin.OUT)
led2 = Pin(16, Pin.OUT)
led3 = Pin(17, Pin.OUT)
led1.value(1)
led2.value(1)
led3.value(1)