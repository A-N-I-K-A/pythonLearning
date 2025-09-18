a=5
b=2

try:
    print("Resource open")
    print(a/b)
    m=int(input("Enter a number:"))
except ValueError as e:
    print("Invalid Input")
except ZeroDivisionError as e:
    print("Can't divide by zero")
except Exception as e:
    print(e)

finally:
    print("Resource closed")