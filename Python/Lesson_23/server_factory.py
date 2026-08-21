from web_server import WebServer
from database_server import DatabaseServer

class ServerFactory:

    @staticmethod
    def create_server(data):
        server_type = data["server_type"]
        hostname = data["hostname"]
        ip = data["ip"]
        operating_system = data["operating_system"]
        status = data["status"]
        services = data["services"]

        if server_type == "web":
            return WebServer(hostname, ip, operating_system, status, services)
        elif server_type == "database":
            return DatabaseServer(hostname, ip, operating_system, status, services)
        else:
            raise ValueError("Unknown server type")
