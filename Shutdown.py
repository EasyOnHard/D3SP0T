from machine import deepsleep
from shared import *

led1 = Pin(25, Pin.OUT)
led2 = Pin(16, Pin.OUT)
led3 = Pin(17, Pin.OUT)
led1.value(1)
led2.value(1)
led3.value(1)
oled.fill(0)
deepsleep()