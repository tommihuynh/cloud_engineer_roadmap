server = input("Server name: ")
status = input("Status: ")

with open("server_log.txt", "a") as file:
    file.write(f"{server}: {status}\n")

print("Log saved.")
