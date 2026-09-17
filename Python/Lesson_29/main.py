from api_client import APIClient


client = APIClient( "http://127.0.0.1:5000")

servers = client.get("/servers")


for server in servers:
    print(server)

new_server = { 
    "hostname": "web-03", 
    "ip": "10.10.10.12", 
    "operating_system": "Ubuntu", 
    "server_type": "web", 
    "services": " nginx", 
    "status": "Running" } 

created_server = client.post("/servers", new_server) 

print("\nCreated server:")
print(created_server)


update_data= { "status": "Running"}

updated_server = client.put( "/servers/web-02", update_data)


print("\nUpdated server:")
print(updated_server)

deleted_server = client.delete("/servers/web-02")

print("\nDeleted server: ")
print(deleted_server)
