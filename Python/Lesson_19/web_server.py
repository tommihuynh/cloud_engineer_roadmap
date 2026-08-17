from server import Server

class WebServer(Server):
    def __init__(self, hostname, ip, operating_system, status, website):
        super().__init__(hostname, ip, operating_system, status)

        self.website = website
    
    def display(self):
        super().display()
        print(f"Website: {self.website}")
    
    def show_website(self):
        print(f"Website: {self.website}")

    def deploy_website(self):
        print(f"Deploying {self.website}...")
