from device import Device


class Fan(Device):
    def start(self):
        if not self._is_on:
            self._is_on = True
            print("Fan has started")

    def stop(self):
        if self._is_on:
            self._is_on = False
            print("Fan has stopped")
