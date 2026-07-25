hostname = input("Hostname: ")
ip = input("IP Address: ")

with open("devices.txt", "a") as file:
    file.write(f"{hostname}, {ip}\n")

print("Device saved")
