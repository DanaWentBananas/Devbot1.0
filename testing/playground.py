import Jetson.GPIO as GPIO
from time import sleep

led = 33
led2=16
led3=32


GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
pwm = GPIO.PWM(led, 100)

for i in range(1000):
    pwm.start(100)
    GPIO.output(led2,0)
    GPIO.output(led3,1)

GPIO.output(led3,0)