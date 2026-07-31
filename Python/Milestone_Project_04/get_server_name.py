
import re

VALID_FORMAT = re.compile(r"^[a-z]{3,10}-[0-9]{2}$")

def get_server_name():
    """Read and validate the server name """
    while True:
        try:
            name = input(f"Enter the server name: ").strip()
        except KeyboardInterrupt:
            print("\n Program cancelled by user.")
            return None
        if name == "":
            print("Server name cannot be empty.")
            continue
        if VALID_FORMAT.match(name):
            return name
        print("Invalid server name. Use the format: abc-01")
