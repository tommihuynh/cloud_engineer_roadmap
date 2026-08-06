
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
        if name == "":
            print("Server name cannot be empty.")
            continue

        is_duplicate = False

        if VALID_FORMAT.match(name):
            for server in servers:
                if server["hostname"] == name:
                    print("Duplicate hostname, please type it again.")
                    is_duplicate = True
                    break

        if not is_duplicate:
            return name

        print("Invalid server name. Use the format: abc-01")
