try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result is {result}")
except ValueError as ve:
    print("Invalid input! Please enter a valid number.")
    print(ve)
    print(ve.args)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
finally:
    print("Execution completed.")
