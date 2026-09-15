import os

api_url = os.getenv("API_BASE_URL", "http://127.0.0.1:5000")

print(f"API URL: {api_url}")
