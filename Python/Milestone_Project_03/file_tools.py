def save_device(name, ip):
    with open("device.txt", "a") as file:
        file.write(f"{name}, {ip}\n")

