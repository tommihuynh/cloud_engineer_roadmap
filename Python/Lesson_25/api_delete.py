import requests


url = "https://jsonplaceholder.typicode.com/posts/1"


data = {
    "id": 1,
    "title": "Updated API automation",
    "body": "This data was updated by Python",
    "userId": 1
}

response = requests.delete( url, json=data)

response.raise_for_status()

code = response.status_code
data = response.json()

print(code)
print(data)
print(response.text)
