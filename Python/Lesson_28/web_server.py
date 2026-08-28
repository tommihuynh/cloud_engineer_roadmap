from server import Server

class WebServer(Server):
    def __init__(self, hostname, ip, operating_system, status, website):
        super().__init__(hostname, ip, operating_system, status)

        self.website = website
    
    def display(self):
        print("=============================")
        print("The Web server information: ")
        print("=============================")
        self.display_common()
        print(f"Website: {self.website}")
        print("-----------------------------")

    def show_website(self):
        print(f"Website: {self.website}")

    def deploy_website(self):
        print(f"Deploying {self.website}...")
