from mind.MQTTHandler import MQTTHandler
from body.minny import Car

car = Car()
# Set the driving mode to manual
car.set_driving_mode('manual')

# Start the MQTT client and wait for messages to control the car's movements
car.drive()


