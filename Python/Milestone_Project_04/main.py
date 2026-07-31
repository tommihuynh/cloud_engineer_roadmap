import get_server_name
import get_status
import save_server


name = get_server_name.get_server_name()
status = get_status.get_status()
save_server.save(name, status)

