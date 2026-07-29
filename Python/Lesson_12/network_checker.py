try:
    print("Connectinh to server...")

except TimeoutError:
    print("Connection time out.")

except ConnectionError:
    print("Unable to connect.")
