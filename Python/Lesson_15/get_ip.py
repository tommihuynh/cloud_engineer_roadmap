import re

VALID_IP = re.compile(r'^10\.10\.10\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$')

def get_ip():
    """ Get and validate the server IP address """
    while True:
        try:
            ip = input(f"Enter the IP Address: ").strip()
        except KeyboardInterrupt:
            print("\n Program cancelled by user.")
            return None

        if VALID_IP.fullmatch(ip):
            return ip
        else:
            print("Invalid IP Address, please try it again.")
            continue
