from web_server import WebServer
from database_server import DatabaseServer
from server_factory import ServerFactory


test = ServerFactory.create_server( "unknown", "web-01", "10.10.10.10", "Ubuntu", "Running", "python.com" )

test.display
