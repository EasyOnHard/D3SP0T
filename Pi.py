from time import sleep
from lib.shared import *

'''
This Program was made by ChatGPT for fun. The most precise it gets is 3.14159297943115 after about 160 iterations (5 Seconds.) It is the same even after 20,000 iterations (10 Minutes)
'''

# Nilakantha Series Calculation
def calculate_pi():
    global button_down
    pi = 3  # Initial term of the Nilakantha series
    sign = 1
    iteration = 1

    while True:
        # Next term in Nilakantha series
        term = (4 / ((2 * iteration) * (2 * iteration + 1) * (2 * iteration + 2))) * sign
        pi += term
        sign *= -1  # Flip sign for next term

        # Display on OLED
        oled.fill(0)
        oled.text("Pi Approximation:", 0, 0, 1)
        oled.text(f"{pi:.15f}", 0, 10, 1)
        oled.text(f"Iter: {iteration}", 0, 20, 1)
        oled.show()

        iteration += 1
        # sleep(1)  # Update every second
        if button_hold(button_down):
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

calculate_pi()
