from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self):
        self._is_on = False  # protected internal state

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    def is_on(self):
        """Read-only access to device state"""
        return self._is_on
