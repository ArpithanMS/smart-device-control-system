from device import Device
class Controller:
    def operate(self, device: Device):
        device.start()
        device.stop()
