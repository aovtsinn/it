# import Raspberry Pi gpio support into python
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

led = 18  # gpio number where the led is connected

# Tell the GPIO module to use gpio numbering used by cpu
GPIO.setmode(GPIO.BCM)
# Set gpio nr 18 to output mode
GPIO.setup(led, GPIO.OUT)

# Blink some leds
while True:
    GPIO.output(led, False)
    sleep(1)  # Sleep for 1 second
    GPIO.output(led, True)
    sleep(1)
