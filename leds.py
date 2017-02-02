import pigpio
from time import sleep

pi = pigpio.pi('192.168.1.12', 8888)        # Connect to the local Pi

pins_used = (17, 27, 22, 18, 23, 24)

for i in pins_used:                         # Sets up pins as outputs
    pi.set_mode(i, pigpio.OUTPUT)

# Assign pins to colors
R1 = 17
G1 = 27
B1 = 22
R2 = 18
G2 = 23
B2 = 24

# Set frequency
Hz = 800 
freq = 1 / Hz # in seconds

def breathe(color, time=1):
    # Reset each color
    for i in pins_used:
        pi.set_PWM_dutycycle(i, 0)
    # Set min and max levels 
    level = pi.get_PWM_dutycycle(color)       
    min_level = 0
    max_level = 255
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