try:
    first = float(input("First number: "))
    second = float(input("Second number: "))
    print(f"Result: {first / second}")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")
