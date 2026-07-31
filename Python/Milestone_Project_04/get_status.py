
VALID_STATUS = [ "Running", "Stopped"]

def get_status():
    try:
        status = input(f"Please enter the server status(Running, Stopped): ")
    except KeyboardInterrupt:
        print("\n Program cancelled by user. ")

    if status is None:
        return
    while True:
        status = input(f"Please enter the server status again")
        if status in VALID_STATUS:
            return status
        print("Invalid status")
