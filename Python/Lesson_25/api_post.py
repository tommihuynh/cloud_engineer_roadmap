import requests


url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My first API automation",
    "body": "Hello from Python",
    "userId": 1

}

response = requests.post( url, json=data)

response.raise_for_status()

result = response.json()

print(result)
