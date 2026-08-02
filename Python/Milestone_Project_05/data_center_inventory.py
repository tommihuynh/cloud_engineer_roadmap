
class Server:
    def __init__(self, hostname, ip, os, ram, cpu, status):
        self.hostname = hostname
        self.ip = ip
        self.os = os
        self.ram = ram
        self.cpu = cpu
        self.status = status

    def display(self):
        print("==========")
        print(f"Hostname: {self.hostname}")
        print(f"IP: {self.ip}")
        print(f"OS: {self.os}")
        print(f"RAM: {self.ram}")
        print(f"CPU: {self.cpu}")
        print(f"Status: {self.status}")
    def restart(self):
        print(f"Restaring {self.hostname}...")

server01 = Server("web-01", "10.0.0.12", "CentOS", "128", "64", "Running")
server02 = Server("web-02", "10.0.0.13", "Ubuntu", "128", "64", "Running")
server03 = Server("db-01", "10.0.0.14", "Ubuntu", "128", "64", "Running")

server01.display()
server02.display()
server03.display()
print()

server01.restart()
server02.restart()
server03.restart()
