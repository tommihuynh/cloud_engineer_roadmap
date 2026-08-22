import requests


try:
    response = requests.get( "https://jsonplaceholder.typicode.com/posts/9999" )
    code = response.status_code
    
    if code == 200:
        print("Request was successfully")
    else:
        print(f"Request failed. Status code {code}.")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}.")

