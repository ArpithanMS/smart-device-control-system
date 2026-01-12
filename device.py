from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self):
        self.__is_on = False  # truly private

    @property
    def is_on(self):
        """Read-only access to device state"""
        return self.__is_on

    def _turn_on(self):
        self.__is_on = True

    def _turn_off(self):
        self.__is_on = False

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
