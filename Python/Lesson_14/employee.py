
import json

employee = [
    {
      "Name": "Trung",
      "Department": "IT Department",
      "Email": "trunghh@gmail.com",
      "Location": "Finland"
    }
]

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

with open("employee.json") as file:
    employees = json.load(file)

print(employees)

