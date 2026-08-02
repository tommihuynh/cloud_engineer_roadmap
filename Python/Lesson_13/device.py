
class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
    def display(self):
        print(f"Device: {self.name}")
        print(f"IP: {self.ip}")


device = Device("Switch-01", "10.0.0.1")
device.display()
print()

