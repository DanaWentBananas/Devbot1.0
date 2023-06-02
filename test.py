import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BCM)
    led_pin = 18

    # Set up GPIO pin for PWM
    GPIO.setup(led_pin, GPIO.OUT)
    pwm_led = GPIO.PWM(led_pin, 100)  # Frequency set to 100Hz

    # Start PWM with 0% duty cycle
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

if __name__ == '__main__':
    main()

