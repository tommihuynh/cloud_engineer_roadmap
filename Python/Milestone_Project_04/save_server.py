import datetime as dt

timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
FILE_NAME = "server_monitor.txt"

def save(name, status):
    """Add the server name and status """
    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"{timestamp}, {name}, {status}\n")
            return True
    except OSError as err:
        print(f"Unable to save the information: {err}")
        return False
