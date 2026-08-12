from server import Server 

def create_server(hostname, ip, os, status):
    """ Create the server information with input"""
    return Server(hostname, ip, os, status)

