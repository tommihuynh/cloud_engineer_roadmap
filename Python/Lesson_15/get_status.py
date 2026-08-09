
VALID_STATUS = { "Running", "Stopped", "Offline", "Maintenance"}

def get_status():
    """ Get and validate the server status """
    while True:
        try:
            status = input(f"Enter the server status (Running, Stopped, Offline, Maintenance): ").strip().capitalize()
        except KeyboardInterrupt:
            print(f"Program cancelled by user.")
            return None

        if status in VALID_STATUS:
            return status
        else:
            print(f"Invalid status, please type it again:")
