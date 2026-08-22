
server = { "hostname": "web-01", "ip": "10.10.10.10"}

print(server["ip"])

print(server.get("status", "Unknown"))
