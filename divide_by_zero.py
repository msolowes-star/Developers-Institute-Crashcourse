try:
    result = 1 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
