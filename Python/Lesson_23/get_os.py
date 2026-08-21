
VALID_OS = { "Ubuntu", "Windows Server"}

def get_os():
    """ Get and validate Operating System"""
    while True:
        try:
            operating_system = input(f"Enter the Operating System: ").strip().title()
        except KeyboardInterrupt:
            print(f"Program cancelled by user.")
            return None

        if operating_system in VALID_OS:
            return operating_system
        else:
            print(f"Invalid the operating system, please try it again: ")
            continue
