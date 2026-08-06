
VALID_STATUS = { "Running", "Stopped", "Offline", "Maintenance"}

def get_status():
    """Read and validate the server status """
    while True:
        try:
            status = input(f"Enter the server status (Running, Stopped, Offline, Maintenance ): ").strip().capitalize()
        except KeyboardInterrupt:
            print("\n Program cancelled by user.")
            return None
        if status in VALID_STATUS:
            return status
        print(f"Invalid status. Please type it again:")
