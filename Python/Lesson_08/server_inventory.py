servers = []
for i in range(3):
    server = input(f"Enter server {i+1}: ")
    servers.append(server)

print("\n===== Server Inventory =====")

for server in servers:
   print(server)

print(f"\nTotal servers: {len(servers)}")
