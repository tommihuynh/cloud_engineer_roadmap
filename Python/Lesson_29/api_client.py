import requests



class APIClient:
    """Request and receive data from a server """
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, method, endpoint, data=None):
        url = self.base_url + endpoint

        response = requests.request(method, url, json=data)

        response.raise_for_status()

        return response.json()

    def get(self, endpoint):
        return self._request("GET", endpoint)

    def post(self, endpoint, data):
        return self._request("POST", endpoint, data)

    def put(self, endpoint, data):
        return self._request("PUT", endpoint, data)
