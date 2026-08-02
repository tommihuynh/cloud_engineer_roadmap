
class Server:
    def __init__(self, hostname, os, ram):
        self.hostname = hostname
        self.os = os
        self.ram = ram

    def show(self):
        print(f"Hostname: {self.hostname}")
        print(f"Operating System: {self.os}")
        print(f"RAM: {self.ram} GB")


server = Server("web-01", "Ubuntu", "16")

server.show()
