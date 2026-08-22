import requests


url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "id": 101,
    "title": "Updated API automation",
    "body": "This data was updated by Python",
    "userId": 1
}

response = requests.put( url, json=data )

response.raise_for_status()

result = response.json()

print(result)

