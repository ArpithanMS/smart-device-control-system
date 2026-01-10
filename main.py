from controller import Controller

from Devices.motor import Motor
from Devices.light import Light
from Devices.fan import Fan


if __name__ == "__main__":
    motor = Motor()
    light = Light()
    fan =  Fan()

    motor_controller = Controller()
    light_controller = Controller()
    fan_controller = Controller()

    motor_controller.operate(motor)
    light_controller.operate(light)
    fan_controller.operate(fan)
