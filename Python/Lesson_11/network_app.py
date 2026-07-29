import network_tools

servers = ["web-01", "web-02", "db-01"]

for server in servers:
    network_tools.ping(server)
