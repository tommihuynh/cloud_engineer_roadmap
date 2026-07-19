def check_server(server_name,status):
    print(f"Checking: {server}...")
    print("Status: {status}")
    print()

servers = [ "web-01", "web-02", "db-01" ]
status = ["Online"]

for server in servers:
    check_server(server,status)
