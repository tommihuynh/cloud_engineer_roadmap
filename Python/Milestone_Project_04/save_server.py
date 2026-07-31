import datetime as dt

def save(name, status):
    """Add the server name and status """
    try:
        with open("server_monitor.txt", "a") as file:
            file.write(f"{dt.datetime.now()}, {name}, {status}\n")
            return True
    except OSError as err:
        print(f"Unable to save the information: {err}")
        return False
