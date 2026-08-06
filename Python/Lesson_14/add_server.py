import json

servers = [ {"hostname": "web-01", "status": "running"}, {"hostname": "db-01", "status": "Stopped"}]

with open("server.json", "a") as file:
    json.dump(servers, file)
