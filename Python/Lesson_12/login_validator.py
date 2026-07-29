password = input("Password: ")

try:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters.")
    print("Password accepted.")

except ValueError as error:
    print(error)
