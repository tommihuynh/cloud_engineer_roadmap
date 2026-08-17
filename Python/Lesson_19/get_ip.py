import re

VALID_IP = re.compile(r'^10\.10\.10\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$')

def get_ip():
    """ Get and validate the server ip address"""
    while True:
        try:
            ip = input(f"Enter the IP address: ").strip()
        except KeyboardInterrupt:
            print(f"\nProgram cancelled by user.")
            return None

        if VALID_IP.fullmatch(ip):
            return ip
        else:
            print(f"Invalid IP Address, please try it again.")
            continue
