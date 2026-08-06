import json

def save_server(server):
    """ Write data into JSON file """
    try:
        with open("servers.json", "w") as file:
            json.dump(server, file, indent=4)
        return True
    except OSError as err:
        print(f"Unable to save the information: {err}")
        return False


