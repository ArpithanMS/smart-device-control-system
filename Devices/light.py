from device import Device

class Light(Device):
    def start(self):
        if not self.is_on:
            self._turn_on()
            print("Light switched on")

    def stop(self):
        if self.is_on:
            self._turn_off()
            print("Light switched off")
