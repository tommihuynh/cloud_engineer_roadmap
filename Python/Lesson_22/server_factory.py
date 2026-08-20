from web_server import WebServer
from database_server import DatabaseServer

class ServerFactory:

    @staticmethod
    def create_server( server_type, hostname, ip, operating_system, status, services):
        if server_type == "web":
            return WebServer(hostname, ip, operating_system, status, services)
        elif server_type == "database":
            return DatabaseServer(hostname, ip, operating_system, status, services)
        else:
            raise ValueError("Unknown server type")
