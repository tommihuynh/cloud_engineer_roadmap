import requests


class APIClient:
    """Request and receive data from a server """
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        try: 
            response = requests.get(self.base_url+endpoint)
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(f"Request failed: {error}") 
            return []
