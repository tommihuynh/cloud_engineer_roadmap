def check_file():
    try:
        with open("server_monitor.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("\n The file is not exist. ")
