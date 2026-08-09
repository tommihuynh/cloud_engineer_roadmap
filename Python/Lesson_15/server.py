

class Server:


    def __init__(self, hostname, ip, operating_system, status):
        self.hostname = hostname
        self.ip = ip
        self.operating_system = operating_system
        self.status = status

    def display(self):
        print("\n==========================") 
        print("The server information: ")
        print("==========================")
        print(f"Hostname: {self.hostname}")
        print(f"IP: {self.ip}")
        print(f"operating_system: {self.operating_system}")
        print(f"Status: {self.status}")
        print("-------------------------")

    def is_running(self):
        if self.status == "Running":
            print(f"\nThe server is running")
            return True
        else:
            print(f"\n The server is not running")
            return False

    def change_status(self, new_status):
        self.status = new_status
        print(f"Server status changed to {self.status}")
   
    def stop(self):
        self.status = "Stopped"
        print(f"{self.hostname} has been stopped.")
