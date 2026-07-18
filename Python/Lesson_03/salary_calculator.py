hourly_rate = float(input("Huorly rate ($): "))
hours = float(input("Hours worked: "))

salary = hourly_rate*hours

print()
print("=====Salary=====")
print(f"Hourly Rate  : ${hourly_rate:.2f}")
print(f"Hourly Worked: {hours}")
print(f"Total Salary : ${salary: .2f}")
