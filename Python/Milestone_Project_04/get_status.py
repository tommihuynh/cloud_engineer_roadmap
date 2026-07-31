
VALID_STATUS = { "Running", "Stopped", "Offline", "Maintenance" }

def get_status():
    """Read and validate the server status """
    while True:
        try:
            status = input(f"Please enter the server status ( running, stopped, offline or maintenance )").strip().capitalize()
        except KeyboardInterrupt:
            print("\n Program cancelled by user. ")
            return None
        if status in VALID_STATUS:
            return status
        print("Invalid status")
