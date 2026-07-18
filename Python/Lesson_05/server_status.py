status = input("Server status (online/offline): ").strip().lower()

if status == "online":
    print("Server is running normally.")
else:
    print("Server is offline. Please investigate.")
