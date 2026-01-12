from device import Device

class Fan(Device):
    def start(self):
        if not self.is_on:
            self._turn_on()
            print("Fan has started")

    def stop(self):
        if self.is_on:
            self._turn_off()
            print("Fan has stopped")
