import os
from dotenv import load_dotenv


load_dotenv()
api_url = os.getenv("API_BASE_URL")

print(f"API URL: {api_url}")
