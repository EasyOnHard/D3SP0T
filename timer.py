from lib.shared import *
from time import ticks_ms, ticks_diff

times = [0,0,0,0,0,0]
line = 0
elapsed_time = 0
last_time = 0
running = False
button_down = False

def display_time(elapsed_time):
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    oled.fill(0)
    oled.text(f"{minutes:02}:{seconds:02}", 40, 20, 1)
    oled.show()

def start():
    global running, last_time
    running = True
    last_time = ticks_ms()

def pause():
    global running
    running = False

def reset():
    global times, line, elapsed_time, last_time, running
    times = [0,0,0,0,0,0]
    line = 0
    elapsed_time = 0
    last_time = 0
    running = False

reset()
display_time(elapsed_time)

while True:
    if button_pin.value() == False and not button_down:  # Button pressed
        button_down = True
        if running:
            pause()
        else:
            start()

    if step_pin.value() == False:  # Reset button pressed
        reset()
        display_time(elapsed_time)

    if running:  # If the stopwatch is running
        current_time = ticks_ms()
        elapsed_time += ticks_diff(current_time, last_time) / 1000
        last_time = current_time
        display_time(elapsed_time)

    if button_pin.value() == True:  # Button released
        button_down = False
    sleep(.01)