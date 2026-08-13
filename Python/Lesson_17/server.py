import re

VALID_STATUS = { "Running", "Stopped", "Offline", "Maintenance"}
VALID_FORMAT = re.compile(r'^[a-z]{3,10}-[0-9]{2}$')

class Server:

    def __init__(self, hostname, ip, operating_system, status):
        self.hostname = hostname
        self.ip = ip
        self.operating_system = operating_system
        self._status = status

    @property
    def hostname(self):
        return self._hostname
    @hostname.setter
    def hostname(self, new_hostname):
        if VALID_FORMAT.fullmatch(new_hostname):
            self._hostname = new_hostname
        else:
            raise ValueError("Invalid server hostname.")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if new_status not in VALID_STATUS:
            raise ValueError("Invalid server status.")

        self._status = new_status


    def display(self):
        print("================================") 
        print("The server information: ")
        print("================================")
        print(f"Hostname: {self.hostname}")
        print(f"IP: {self.ip}")
        print(f"OS: {self.operating_system}")
        print(f"Status: {self.status}")
        print("--------------------------------")

    def is_running(self):
        if self.status == "Running":
            return True
        return False

    def change_status(self, new_status):
        try:
            self.status = new_status
            print(f"{self.hostname} status changed to {self.status}.")
            return True
        except ValueError:
            print("Invalid status")
            return False

    def start(self):
        self.status = "Running"
        print(f"{self.hostname} is starting.")

    def stop(self):
        self.status = "Stopped"
        print(f"{self.hostname} has been stopped.")

    def reboot(self):
        if self.is_running():
            print(f"{self.hostname} is rebooting... ")
            self.stop()
            self.start()
            print(f"{self.hostname} has been reboot successfull. ")
            return True
        return False
