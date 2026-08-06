import json

switch = { "Hostname": "sw-01", "IP": "10.10.10.10", "Vendor": "Cisco", "Model": "x2028" }

with open("switch.json", "w") as file:
    json.dump(switch, file, indent=4)

with open("switch.json") as file:
    switch = json.load(file)

print(f"Switch Information")
print(f"------------------")
print(switch)
