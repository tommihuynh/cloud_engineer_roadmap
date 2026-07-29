

import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQTUVWXY0123456789"
special = "!@#$%"
password = ""

for i in range(5):
    password += random.choice(characters) + random.choice(special) 

print("Generated password: ")
print(password)

