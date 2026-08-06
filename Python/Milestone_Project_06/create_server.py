

def create_server(hostname, ip, operating_system, status):
    """ Write data into JSON file """
    return  {
        "hostname": hostname,
        "ip": ip,
        "operating_system": operating_system,
        "status": status
    } 


