import RPi.GPIO as GPIO
from mind.mqttHandler import MQTTHandler
import os
from dotenv import load_dotenv

load_dotenv()
# leftA = os.getenv("leftA")
# leftB = os.getenv("leftA")
# rightA = os.getenv("rightA")
# rightB = os.getenv("rightB")
leftA = 12
leftB = 13
rightA = 16
rightB = 33

class Car:
    def __init__(self):
        # Set up GPIO pins for the car's wheels
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(leftA, GPIO.OUT)
        GPIO.setup(leftB, GPIO.OUT)
        GPIO.setup(rightA, GPIO.OUT)
        GPIO.setup(rightB, GPIO.OUT)
        # self.left_motor_pwm = GPIO.PWM(leftA, 50)
        # self.right_motor_pwm = GPIO.PWM(rightA, 50)
        # self.left_motor_pwm.start(0)
        # self.right_motor_pwm.start(0)
        # self.speed = 60
        
        # Set initial driving mode to manual
        self.driving_mode = 'manual'
        
        # Set up flag variable for controlling loop in drive method
        self.running = True
        
        # Create MQTT handler object
        self.mqtt_handler = MQTTHandler(self)

    def set_speed(self, speed):
        if speed >= 0 and speed <= 100:
            self.speed = speed
        
    def forward(self):
        if self.driving_mode == 'manual':
            # self.left_motor_pwm.ChangeDutyCycle(self.speed)
            GPIO.output(leftA, GPIO.LOW)
            GPIO.output(leftB, GPIO.HIGH)
            #self.right_motor_pwm.ChangeDutyCycle(self.speed)
            GPIO.output(rightA, GPIO.LOW)
            GPIO.output(rightB, GPIO.HIGH)
        else:
            # Code for automatic driving mode
            pass
        
    def turn_left(self):
        if self.driving_mode == 'manual':
            # self.left_motor_pwm.ChangeDutyCycle(self.speed)
            GPIO.output(leftA, GPIO.LOW)
            GPIO.output(leftB, GPIO.LOW)
            # self.right_motor_pwm.ChangeDutyCycle(self.speed)
            GPIO.output(rightA, GPIO.LOW)
            GPIO.output(rightB, GPIO.HIGH)
            pass
        else:
            # Code for automatic driving mode
            pass
        
    def turn_right(self):
        if self.driving_mode == 'manual':
            # self.left_motor_pwm.ChangeDutyCycle(self.speed)
            GPIO.output(leftA, GPIO.LOW)
            GPIO.output(leftB, GPIO.HIGH)
            # self.right_motor_pwm.ChangeDutyCycle(self.speed)
            GPIO.output(rightA, GPIO.LOW)
            GPIO.output(rightB, GPIO.LOW)
            pass
        else:
            # Code for automatic driving mode
            pass
        
    def stop_driving(self):
        if self.driving_mode == 'manual':
            # self.left_motor_pwm.ChangeDutyCycle(0)
            GPIO.output(leftA, GPIO.LOW)
            GPIO.output(leftB, GPIO.LOW)
            # self.right_motor_pwm.ChangeDutyCycle(0)
            GPIO.output(rightA, GPIO.LOW)
            GPIO.output(rightB, GPIO.LOW)
        else:
            # Code for automatic driving mode
            pass
        
    def set_driving_mode(self, mode):
        self.driving_mode = mode
        
    def drive(self):
        # Start the MQTT handler
        self.mqtt_handler.start()
        
        while self.running:
            pass  # You can add logic for handling other messages here
            
        # Stop the MQTT handler when driving ends
        self.mqtt_handler.stop()
    
    def stop(self):
        self.running = False
