Python Lab Practical Practice

A repository consisting of 10 Python scripts created for practice ahead of a lab practical exam. The programs consist of basic control structures and advanced data manipulation using popular data science libraries.

Programs Included
Program 1: To find the largest integer among three numbers using conditional (ternary) operators.
Program 2: To calculate the product of two matrices using nested for loops.
Program 3: To implement basic control structures (if-elif-else) in order to calculate grades based on entered marks.
Program 4: To reshape a DataFrame using the pivot_table function in Pandas.
Program 5: To select particular array elements using fancy indexing in NumPy.
Program 6: To demonstrate exception handling using try, except (ZeroDivisionError, ValueError), else, and finally blocks.
Program 7: To explore Object-Oriented Programming (OOP) by defining a Car class with __init__ attributes and display methods.
Program 8: To utilize NumPy library functions for array operations such as shape, datatype, sum, mean, min, max, square root, reshape, sort, and random integer generation.
Program 9: To use Pandas library functions to create DataFrames, check shapes, filter data, add new columns, sort values, and calculate column averages.
Program 10: To demonstrate machine learning library functions using Scikit-Learn (make_blobs) and visualize data using Matplotlib scatter plots.

Technologies & Libraries Used

Python
Pandas
NumPy
Scikit-Learn
Matplotlib

Concepts Practiced
Conditional operators and logic
Nested loops and matrix multiplication
if-elif-else control structures
Data reshaping and pivot tables
Arrays and fancy indexing
Error and exception handling
Object-Oriented Programming (Classes, Objects, Methods)
DataFrame filtering, sorting, and manipulation
Data visualization and scatter plotting

Example
== Exception Handling (Program 6) ==

Python
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

How to Run
1. Clone the Repository
   
Bash
git clone https://github.com/your-username/python-lab-exam-practice.git

3. Install Required Libraries
Ensure that you have the necessary data science libraries installed:

Bash
pip install pandas numpy scikit-learn matplotlib

5. Open the Project Folder
Bash
cd python-lab-exam-practice

7. Run the Programs
Bash
python "1st Program.py"
python "10th Program.py"

Project Structure
Plaintext
python-lab-exam-practice/
│
Day 4
├── 1st Program.py
├── 2nd Program.py
├── 3rd program.py
├── 4th Program.py
├── 5th Program.py
├── 6th Program.py
├── 7th Program.py
├── 8th Program.py
├── 9th Program.py
├── 10th Program.py
└── README.md

Learning Purpose
This project was created as a focused study session to practice and review Python programming concepts in preparation for an upcoming lab practical exam. This repository builds on foundational knowledge in basic scripting, object-oriented principles, and data analysis workflows

Author
Muneeswaran P
B.Sc. Artificial Intelligence and Machine Learning Student
