import serial
import time

class arduinoBridge:
    def __init__(self, serial_port, baud_rate):
        self.ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2)  # Allow time for the serial connection to establish

    def send_command(self, command):
        self.ser.write(command.encode())
        time.sleep(0.1)  # Delay to allow Arduino to process the command

    def close(self):
        self.ser.close()
