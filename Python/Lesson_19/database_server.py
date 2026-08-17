from server import Server

class DatabaseServer(Server):
    def __init__( self, hostname, ip, operating_system, status, database):
        super().__init__( hostname, ip, operating_system, status)
        self.database = database

    def display(self):
        super().display()
        print(f"Database: {self.database}")


