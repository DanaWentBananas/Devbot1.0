import RPi.GPIO as GPIO
import time
import os
from dotenv import load_dotenv

GPIO.setmode(GPIO.BCM)

load_dotenv()
leftA = os.getenv("leftA")
leftB = os.getenv("leftA")
rightA = os.getenv("rightA")
rightB = os.getenv("rightB")
led_pin = 18


def goForward():
    pass

def turnLeft():
    print("im inside left")
    GPIO.setup(led_pin, GPIO.OUT)
    pwm_led = GPIO.PWM(led_pin, 100)
    pwm_led.start(0)

    # Increase the LED brightness gradually
    for duty_cycle in range(0, 101, 5):
        pwm_led.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)

    # Wait for a few seconds with maximum brightness
    time.sleep(2)

    # Decrease the LED brightness gradually
    for duty_cycle in range(100, -1, -5):
        pwm_led.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)

    # Stop PWM
    pwm_led.stop()

    # Clean up GPIO
    GPIO.cleanup()

def turnRight():
    pass

def stopMoving():
    pass