from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_on(self):
        print("Smartphone is turning on with a button press")
    
    def turn_off(self):
        print("Laptop is shutting down fromt he start menu.")

    def restart(self):
        print("Laptop is restarting from the start menu.")
#usage
devices = [Smartphone(), Laptop()]

for device in devices:
    device.turn_on()
    device.restart()
    device.turn_off()

