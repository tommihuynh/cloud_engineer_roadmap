import sys
from get_hostname import get_hostname
from get_ip import get_ip
from get_os import get_os
from get_status import get_status
from create_server import create_server
from server import Server


name = get_hostname()

if name is None:
    sys.exit(1)

ip = get_ip()
if ip is None:
    sys.exit(1)

operating_system = get_os()
if operating_system is None:
    sys.exit(1)

status = get_status()
if status is None:
    sys.exit(1)


server = create_server(name, ip, operating_system, status)
print()
server.display()
print()
"""server.hostname = "Hello" """
"""server.status = "Hello" """

server.change_status("Maintenance")
print()
server.display()
print()
"""
server.reboot()
"""
