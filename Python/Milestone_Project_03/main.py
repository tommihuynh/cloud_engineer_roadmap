import device_tools
import file_tools
import network_tools

name = input("Hostname: ")
ip = input("IP Address: ")

device_tools.show_device(name, ip)
file_tools.save_device(name, ip)
network_tools.ping_device(name)

