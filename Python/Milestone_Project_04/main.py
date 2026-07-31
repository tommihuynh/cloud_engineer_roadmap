from get_server_name import get_server_name
from get_status import get_status
from save_server import save


name = get_server_name()

if name is None:
    exit()

status = get_status()

if status is None:
    exit()

if save(name, status):
    print("Server information saved successfully. ")
else:
    print("Server information save failed. ")
