import os
from dotenv import load_dotenv
import logging
from api_client import APIClient
from server_factory import ServerFactory
from logging.handlers import RotatingFileHandler


handler = RotatingFileHandler(
    "logs/server_health.log",
    maxBytes=1000,
    backupCount=3
)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

load_dotenv()

api_url = os.getenv("API_BASE_URL")

if not api_url:
    raise ValueError("API_BASE_URL is not configured")

client = APIClient(api_url)

servers_data = client.get("/servers")

servers = [ ServerFactory.create_server(data) for data in servers_data ]

healthy = 0
problems = 0
problem_servers = []

logger.info("Server health check started.")

for server in servers:
    if server.is_running():
        healthy += 1
        print(f"{server.hostname}: OK. ")
        logger.info(f"{server.hostname} is running.")
    else:
        problems += 1
        problem_servers.append(server)
        print(f"{server.hostname}: PROBLEM.")
        logger.warning(f"{server.hostname} is stopped. ")

logger.info("Server health check finished.")


print()
print("==============================")
print("Server healthy summary:")
print("==============================")
print(f"Total servers: {len(servers)}")
print(f"Healthy: {healthy}")
print(f"Problems: {problems}")

