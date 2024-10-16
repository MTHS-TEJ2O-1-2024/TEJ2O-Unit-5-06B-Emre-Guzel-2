"""
Created by: Emre Guzel
Created on: Oct 16 2024
This module is a Micro:bit MicroPython program claculates the distance 
"""

from microbit import *


# Idenfiyng the sonar class and asingning the sonor
class HCSR04:
    sonar = HCSR04()
    display.show(Image.HAPPY)

    while True():
    # Finding the distance
        if button_a.is_pressed():
            display.clear()
