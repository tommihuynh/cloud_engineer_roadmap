
import re

VALID_FORMAT = re.compile(r'^[a-z]{3,10}-[0-9]{2}$')

def get_hostname(servers):
    """Read and validate the server name """
    while True:
        try:
            name = input(f"Enter the server name: ").strip().lower()
        except KeyboardInterrupt:
            print("\n Program cancelled by user.")
            return None

        if VALID_FORMAT.match(name):
            if any(server["hostname"] == name for server in servers):
                print("Duplicate hostname, please type it again.")
                continue
            return name
        else:
            print("Invalid server name. Use the format: abc-01")
