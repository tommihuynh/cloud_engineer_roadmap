
def save(name, status):
    with open("server_monitor.txt", "a") as file:
        file.write(f"{name}, {status}\n")
        print("Hi, the server information saved successfully ")
