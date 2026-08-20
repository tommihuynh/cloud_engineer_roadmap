from server_factory import ServerFactory


web = ServerFactory.create_server( "web", "web-01", "10.10.10.10", "Ubuntu", "Running", "python.com" )

database = ServerFactory.create_server( "database", "dbb-01", "10.10.10.20", "Ubuntu", "Running", "MySQL" )


servers = [ web, database]


for server in servers:
    server.display()
    print()

for server in servers:
    if server.is_running():
        print(f"{server.hostname} is running.")
    else:
        print(f"{server.hostname} is not running.")

