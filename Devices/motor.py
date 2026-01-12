from device import Device

class Motor(Device):
    def start(self):
        if not self.is_on:
            self._turn_on()
            print("Motor has started")

    def stop(self):
        if self.is_on:
            self._turn_off()
            print("Motor has stopped")
