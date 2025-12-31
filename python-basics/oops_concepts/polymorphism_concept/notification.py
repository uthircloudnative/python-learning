from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, msg):
        pass # This is abstractmethod implementation will be done by child classes