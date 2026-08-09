import sys
from load_servers import load_servers
from get_hostname import get_hostname
from get_ip import get_ip
from get_os import get_os
from get_status import get_status
from save_server import save_server
from create_server import create_server

servers = load_servers()

name = get_hostname(servers)
if name is None:
    sys.exit(1)

ip = get_ip(servers)
if ip is None:
   sys.exit(1)

operating_system = get_os()
if operating_system is None:
    sys.exit(1)

status = get_status()
if status is None:
    sys.exit(1)

new_server = create_server(name, ip, operating_system, status)

servers.append(new_server)

if save_server(servers):
    print("Server information saved successfully. ")
else:
    print("Failed to save server information. ")




