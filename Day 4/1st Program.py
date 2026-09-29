# 1.Write a python program to find the largest integer using conditional operator

a = int(input("\nEnter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))

lar = a if a>b and a>c else(b if b>c else c)

print(f"\nThe Largest number among 'a','b'and'c' is : {lar}")