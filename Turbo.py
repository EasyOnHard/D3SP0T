from shared import *
from machine import freq

def display_freq(CLOCK_SPEED):
    oled.fill(0)
    oled.text(f"{CLOCK_SPEED / 1000000}MHz", 35, 20, 1)
    oled.show()

def loop():
    global button_down
    while True:
        if previous_value != step_pin.value():
            if step_pin.value() == False:

                if direction_pin.value() == False:
                    CLOCK_SPEED = freq()
                    if CLOCK_SPEED > MIN_CLOCK:
                        CLOCK_SPEED -= 1000000
                        freq(CLOCK_SPEED)
                    else:
                        pass
                    
                else:
                    CLOCK_SPEED = freq()
                    if CLOCK_SPEED < MAX_CLOCK:
                        CLOCK_SPEED += 1000000
                        freq(CLOCK_SPEED)
                        
                CLOCK_SPEED = freq()
                display_freq(CLOCK_SPEED)
                sleep(0.01)

        if button_hold(button_down) == "Press":
            freq(125000000)
            CLOCK_SPEED = freq()
            sleep(.01)
            display_freq(CLOCK_SPEED)
        elif button_hold(button_down):
            from sys import exit
            sleep(.5)
            oled.fill(0)
            oled.text("Release Encoder",5,26)
            oled.show()
            while True:
                if button_hold(button_down) == False:
                    break
            exit()

        if button_pin.value() == True and not button_down:
            button_down = False


display_freq(CLOCK_SPEED)
loop()