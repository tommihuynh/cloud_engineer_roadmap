
def get_server_name():
    try:
        name = input(f"Enter the server name: ")
    except KeyboardInterrupt:
        print("\n Program cancelled by user.")
    if name is None:
        return
    return name
