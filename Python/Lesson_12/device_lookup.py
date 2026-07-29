devices = {"web-01": "10.0.0.5", "db-01": "10.0.0.6"}

device = input("Enter device name: ")

try:
    print(f"IP address: {devices[device]}")
except KeyError:
    print("Device not found.")
