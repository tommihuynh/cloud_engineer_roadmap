import json

def load_servers():
    """ Load the servers information """
    try:
        with open("servers.json", "r") as file:
            server = json.load(file)
            return server
    except FileNotFoundError:
        print("\n The file is not exist")
