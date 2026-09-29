#6. Write a program to demonstrate exception handling

try:
    num1 = float(input("\nEnter First Number:"))
    num2 = float(input("\nEnter Second Number:"))
    ans = num1/num2
    
except ZeroDivisionError:
    print("\nError: Cannot Divide by Zero")
except ValueError:
    print("\nError : Numbers Only Allowed!")
else:
    print(f"\nResult:{ans}")
finally:
    print("\nException Program was Completed!")