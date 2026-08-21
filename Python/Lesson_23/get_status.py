
VALID_STATUS = { "Running", "Stopped", "Offline", "Maintenance"}

def get_status():
    """ Get and validate the status of server. """
    while True:
        try:
            status = input(f"Enter the server status: ").strip().capitalize()
        except KeyboardInterrupt:
            print(f"\nProgram cancelled by the user.")
            return None
        if status in VALID_STATUS:
            return status
        else:
            print(f"Invalid the status, please try it again: ")
            continue
