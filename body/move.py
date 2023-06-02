import RPi.GPIO as GPIO
import time
import os
from dotenv import Dotenv
dotenv = Dotenv('/home/pi/Devbot1.0/.env') 
os.environ.update(dotenv)

GPIO.setmode(GPIO.BCM)

ignition = os.getenv("green")
direction = os.getenv("white")
speed = os.getenv("blue")

GPIO.setup(ignition, GPIO.OUT)
GPIO.setup(direction, GPIO.OUT)
GPIO.setup(speed, GPIO.OUT)

pwm_speed = GPIO.PWM(speed,100)


def goForward(speed):
    pass

def turnLeft(speed):
    print("im inside left")
    GPIO.output(ignition,GPIO.HIGH)
    pwm_speed.start(0)

    # Increase the LED brightness gradually
    for duty_cycle in range(0, 101, 5):
        pwm_speed.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)
        
    stopMoving()



def turnRight():
    pass

def stopMoving():
    GPIO.output(ignition, GPIO.LOW)