def restart_server(server):
    print(f"Restaring {server}...")

servers = ["web-01", "web-02", "db-01"]

for server in servers:
    restart_server(server)
