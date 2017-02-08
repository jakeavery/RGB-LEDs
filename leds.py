import pigpio
from time import sleep
from tkinter import *
from tkinter.colorchooser import *

pi = pigpio.pi('192.168.1.12', 8888)        # Connect to the local Pi

pins_used = (17, 27, 22, 18, 23, 24)

for i in pins_used:                         # Sets up pins as outputs
    pi.set_mode(i, pigpio.OUTPUT)

# Assign pins to strips and colors
strip1 = (17, 27, 22)
strip2 = (18, 23, 24)

# Set frequency
Hz = 800 
freq = 1 / Hz # in seconds

# Set min and max levels
min_level = 0
max_level = 255

def breathe(color, time=1):
    # Reset each color
    for i in pins_used:
        pi.set_PWM_dutycycle(i, 0)
    # Get initial level 
    level = pi.get_PWM_dutycycle(color)       
    # Determine steps needed and amount to change each step
    steps = time / freq
    delta = (max_level - min_level) / steps
    # Loop
    while True:
        level += delta
        if level < min_level or level > max_level:
            delta = -delta
        pi.set_PWM_dutycycle(color, level)
        print(level)
        sleep(freq)
        
color1 = [255, 83, 13]
color2 = [255, 13, 255]
       
def fade(color1=color1, color2=color2, time=1, strip=3):
    # Reset each color
    for i in pins_used:
        pi.set_PWM_dutycycle(i, 0)
    strip1_levels = [0, 0, 0]
    strip2_levels = [0, 0, 0]
    # Determine steps needed
    steps = time / freq
    # Initialize delta list
    delta = [0, 0, 0]
    # Get initial levels
    for i in range(3):
        strip1_levels[i] = pi.get_PWM_dutycycle(strip1[i])
        strip2_levels[i] = pi.get_PWM_dutycycle(strip2[i])
        # Determine amount to change each step
        delta[i] = (color2[i] - color1[i]) / steps
    # Loop
    while True:
        for i in range(3):
            # Strip 1
            if strip == 1 or strip == 3:
                strip1_levels[i] += delta[i]
                if strip1_levels[i] < min_level or strip1_levels[i] > max_level:
                    delta[i] = -delta[i]
                pi.set_PWM_dutycycle(strip1[i], strip1_levels[i])
             # Strip 2
            if strip == 2 or strip == 3:
                strip2_levels[i] += delta[i]
                if strip2_levels[i] < min_level or strip1_levels[i] > max_level:
                    delta[i] = -delta[i]
                pi.set_PWM_dutycycle(strip2[i], strip2_levels[i])   
        sleep(freq)

def getColor():
    color = askcolor()
    rgb = color[0]
    red = int(rgb[0])
    green = int(rgb[1])
    blue = int(rgb[2])
    pi.set_PWM_dutycycle(strip1[0], red)
    pi.set_PWM_dutycycle(strip1[1], green)
    pi.set_PWM_dutycycle(strip1[2], blue)

def setBoth():
    color = askcolor()
    rgb = color[0]
    red = int(rgb[0])
    green = int(rgb[1])
    blue = int(rgb[2])
    # Strip 1
    pi.set_PWM_dutycycle(strip1[0], red)
    pi.set_PWM_dutycycle(strip1[1], green)
    pi.set_PWM_dutycycle(strip1[2], blue)
    # Strip 2
    pi.set_PWM_dutycycle(strip2[0], red)
    pi.set_PWM_dutycycle(strip2[1], green)
    pi.set_PWM_dutycycle(strip2[2], blue)

def setStripOne():
    color = askcolor()
    rgb = color[0]
    red = int(rgb[0])
    green = int(rgb[1])
    blue = int(rgb[2])
    # Strip 1
    pi.set_PWM_dutycycle(strip1[0], red)
    pi.set_PWM_dutycycle(strip1[1], green)
    pi.set_PWM_dutycycle(strip1[2], blue)
    
def setStripTwo():
    color = askcolor()
    rgb = color[0]
    red = int(rgb[0])
    green = int(rgb[1])
    blue = int(rgb[2])
    # Strip 2
    pi.set_PWM_dutycycle(strip2[0], red)
    pi.set_PWM_dutycycle(strip2[1], green)
    pi.set_PWM_dutycycle(strip2[2], blue)
    
def lightsOff():
    # Strip 1
    pi.set_PWM_dutycycle(strip1[0], 0)
    pi.set_PWM_dutycycle(strip1[1], 0)
    pi.set_PWM_dutycycle(strip1[2], 0)
    # Strip 2
    pi.set_PWM_dutycycle(strip2[0], 0)
    pi.set_PWM_dutycycle(strip2[1], 0)
    pi.set_PWM_dutycycle(strip2[2], 0)
    

    