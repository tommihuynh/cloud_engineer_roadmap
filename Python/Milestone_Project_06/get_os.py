

VALID_OS = { "Ubuntu", "Windows Server" }

def get_os():
    """Read and validate the server operating system """
    while True:
        try:
            operating_system = input(f"Enter the Operating System( Ubuntu, Windows Server ): ").strip().title()
        except KeyboardInterrupt:
            print("\n Program cancelled by user.")
            return None
        if operating_system in VALID_OS:
            return operating_system
        print(f"Invalid server os. Please type it again.")
