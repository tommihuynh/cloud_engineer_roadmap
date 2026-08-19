from web_server import WebServer
from database_server import DatabaseServer



web = WebServer( "web-01", "10.10.10.10", "Ubuntu", "Running", "python.com")

database = DatabaseServer( "dbb-01", "10.10.10.20", "Ubuntu", "Running", "MySQL")

servers = [ web, database]



for server in servers:
    server.display()
    print()

for server in servers:
    if server.is_running():
        print(f"{server.hostname} is running.")
    else:
        print(f"{server.hostname} is not running.")
