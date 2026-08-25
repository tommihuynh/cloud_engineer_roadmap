from api_client import APIClient
from server_factory import ServerFactory


client = APIClient( "http://127.0.0.1:5000")

servers_data = client.get("/servers")

servers = []

for data in servers_data:
   server = ServerFactory.create_server(data)
   servers.append(server)

for server in servers:
    server.display()
    print()

for server in servers:
    if server.is_running():
        print(f"{server.hostname} is running. ")
    else:
        print(f"{server.hostname} is not running. ")

