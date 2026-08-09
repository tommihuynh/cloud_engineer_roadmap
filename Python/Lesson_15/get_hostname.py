import re

VALID_FORMAT =re.compile(r'^[a-z]{3,10}-[0-9]{2}$')


def get_hostname():
    "Get and validate the server hostname."
    while True:
        try:
            name = input(f"Enter the server hostname: ").strip().lower()
        except KeyboardInterrupt:
            print("\n Program cancel by user.")
            return None

        if VALID_FORMAT.fullmatch(name):
            return name
        else:
            print("Invalid server name. Use the format: abc-01")
