
from server_factory import ServerFactory

web_data = {
    "server_type": "web",
    "hostname": "web-01",
    "ip": "10.10.10.10",
    "operating_system": "Ubuntu",
    "status": "Running",
    "services": "python.com"
}

database_data = {
    "server_type": "database",
    "hostname": "dbb-01",
    "ip": "10.10.10.20",
    "operating_system": "Ubuntu",
    "status": "Running",
    "services": "MySQL"
}


web = ServerFactory.create_server(web_data)
database = ServerFactory.create_server(database_data)

servers = [ web, database]

for server in servers:
    server.display()
    print()
for server in servers:
    if server.is_running():
        print(f"{server.hostname} is running.")
    else:
        print(f"{server.hostname} is not running.")

