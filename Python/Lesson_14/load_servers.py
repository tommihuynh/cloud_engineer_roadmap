import json

with open("server.json") as file:
    servers = json.load(file)

for server in servers:
    print(server["hostname"])

print(servers)
