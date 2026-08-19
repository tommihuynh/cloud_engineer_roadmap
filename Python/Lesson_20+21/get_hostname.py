
import re

VALID_FORMAT = re.compile(r'^[a-z]{3,10}-[0-9]{2}$')

def get_hostname():
    """ Get and validate the server name. """
    while True:
        try:
            name = input(f"Enter the server name (abc-01): ").strip().lower()
        except KeyboardInterrupt:
            print(f"\nProgram cancelled by user.")
            return None

        if VALID_FORMAT.fullmatch(name):
            return name
        else:
            print(f"Invalid server name, please try it again.")
            continue
