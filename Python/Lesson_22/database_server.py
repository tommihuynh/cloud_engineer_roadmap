from server import Server

class DatabaseServer(Server):
    def __init__( self, hostname, ip, operating_system, status, database):
        super().__init__( hostname, ip, operating_system, status)
        self.database = database

    def display(self):
        print("=============================")
        print("The Database server information: ")
        print("=============================")
        self.display_common()
        print(f"Database: {self.database}")
        print("-----------------------------")



