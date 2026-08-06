import re

VALID_IP = re.compile(r'^10\.10\.10\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$')

def get_ip(servers):
    """Read and validate the server IP Address """
    while True:
        try:
            ip = input(f"Enter the IP Address (10.10.10.xxx): ").strip()
        except KeyboardInterrupt:
            print("\n Program cancelled by user.")
            return None
        if not VALID_IP.match(ip):
            print("Invlaid server ip. Please type it again")
            continue 
        if any(server["ip"] ==ip for server in servers):
            print("Duplicate IP, please type it again.")
            continue
        return ip
  
