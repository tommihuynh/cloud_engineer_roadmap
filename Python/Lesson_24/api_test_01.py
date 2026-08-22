import requests


try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response.raise_for_status()

    data = response.json()
    print(f"User ID: {data.get('userId')}")
    print(f"ID: {data.get('id')}")
    print(f"Title: {data.get('title', 'No title available')}")
    print(f"Body: {data.get('body')}")
    print(f"Description: {data.get('description', 'No description available')}")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")

