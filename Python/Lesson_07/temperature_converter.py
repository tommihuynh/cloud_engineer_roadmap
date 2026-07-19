def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32

print()
temperature = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(temperature)

print()
print(f"{temperature}C = {fahrenheit:.1f}F")
print()
