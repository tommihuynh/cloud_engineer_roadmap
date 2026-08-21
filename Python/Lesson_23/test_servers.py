import json
from server_factory import ServerFactory


with open("servers.json", encoding="utf-8") as file:
    servers_data = json.load(file)

for data in servers_data:
    server = ServerFactory.create_server(data)
    server.display()
    print()
