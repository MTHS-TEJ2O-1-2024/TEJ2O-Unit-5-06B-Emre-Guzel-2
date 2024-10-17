"""
Created by: Emre Guzel
Created on: Oct 16 2024
This module is a Micro:bit MicroPython program claculates the distance 
"""

from microbit import *
#class HCSR04:
sonar = HCSR04()

# Dfeinding the distance
distance_TO_Object = 0
display.show(Image.HAPPY)

if button_a.is_pressed():
    display.clear()
    distance_TO_Object = sonar.ping
