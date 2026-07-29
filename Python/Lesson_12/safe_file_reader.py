filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("That file does not exist")
