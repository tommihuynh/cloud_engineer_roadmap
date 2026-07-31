valid_status = [ "Running", "Stopped" ]

try:
    name = input(f"Please enter the server name (aaa-bb, a is character and b is number): ")
    status = input(f"Please enter the server status(Running, Stopped): ")
except KeyboardInterrupt:
    print("\n Program cancelled by user. ")

if name or status is None:
    return

if status not in valid_status:
    print("The server status is not valid. ")
    while True:
        status = input(f"Please enter the server status again: ")
        if status in valid_status:
            break
try:
    with open("server_monitor.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("\n The file doesn't exist. ") 

with open("server_monitor.txt", "a") as file:
    file.write(f"{name}, {status}.\n")


print("Hi, the server information saved successfully ")


