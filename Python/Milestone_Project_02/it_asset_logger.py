print("Please enter your device information as below step: ")
hostname = input("Hostname: ")
ip = input("Ip Address: ")
os = input("Operating System: ")
ram = input("RAM: ")
cpu = input("CPU: ")

with open("assets.txt", "a") as file:
    file.write(f"{hostname},{ip},{os},{ram} GB,{cpu} cores \n")
    print("The device had been added. ")

question = input("Would you like to view all saved assets?(yes/no):")

if question == "yes":
    with open("assets.txt", "r") as file:
        for line in file:
            print(line.strip())
else:
    print("Have a nice day! ")  
