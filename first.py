import RPi.GPIO as gpio
import time
pin = 15

def main():
    x=1
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin,gpio.OUT, initial=gpio.HIGH)

    print("LED ON")
    try:
        while x==1:
            gpio.output(pin, 1)
            time.sleep(3)
            gpio.output(pin, 0)
            x=2
    finally:
        gpio.cleanup()

if __name__ == '__main__':
    main()
