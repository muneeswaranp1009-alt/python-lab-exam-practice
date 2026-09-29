#3. Write a python program using basic control structures

marks = int(input("\nEnter the mark:"))

if marks < 0 or marks > 100:
    print("\nInvalid Mark!,Enter between 0 and 100")
elif marks >= 90:
    print('Grade: O (Outstanding)')
elif marks >= 80:
    print('Grade: A+ (Excellent)')
elif marks >= 70:
    print('Grade: A (Very Good)')
elif marks >= 60:
    print('Grade: B+ (Good)')
elif marks >= 50:
    print('Grade: B (Above Average)')
elif marks >= 40:
    print('Grade: C (Pass)')
else:
    print('Grade: F (Fail - Below Pass Mark)')