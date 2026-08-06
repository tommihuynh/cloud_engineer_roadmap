import json

server = { "hostname": "db-01", "ip": "10.0.0.101", "status": "Stopped" }

with open("server.json", "w") as file:
    json.dump(server, file, indent=4)

