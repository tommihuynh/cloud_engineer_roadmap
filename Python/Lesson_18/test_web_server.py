from web_server import WebServer


server = WebServer( "web-01", "10.10.10.10", "Ubuntu", "Running", "python.com" )

print()
server.display()
print()
server.show_website()
print()
server.deploy_website()
print()
server.reboot()
