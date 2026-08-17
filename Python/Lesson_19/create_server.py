from server import Server 

def create_server(hostname, ip, operating_system, status):
    """ Create the server information with input"""
    return Server(hostname, ip, operating_system, status)

