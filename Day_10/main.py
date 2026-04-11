## Here math_utils is module
import math_utils as m
print(m.add(3,5))
print(m.multiple(3,5))
print(m.PI)
from math_utils import add
print(add(10,5))

## Lets discuss about Packages (Package is folder where related modules are found.)
### """
# my_school/                <-- Package (folder)
#          __init__.py      <-- Zaroori file - folder ko bnati hai
#          student.py       <-- Module
#          school.py        <-- Module
#          exceptions.py    <-- Module
# This is how can we import:
# from my_school.student import Student
# from my_school.exceptions import InvalidMarksError
# Lets discuss about useful built-in Modules
# import os               --> file system operations
# import sys              --> system operations
# import datetime         --> date and time
# import random           --> random numbers
# import math             --> mathematical funcions

# Examples:
# print(os.getcwd())            --> current directory
# print(datetime.date.today())  --> today's Date
# print(random.randint(0,100))  --> random number
# print(math.sqrt(16))          --> 4.0            """
from student_management.student import Student
from student_management.school import School
from student_management.exceptions import (InvalidMarksError,DuplicateSubjectError,StudentNotFoundError)

school = School("Al-Hassan Academy")
school.load_from_file("school_data.json")

s1 = Student("Hassan",21,"CS-201")
s1.add_marks("Programming Fundamentals",90)
s1.add_marks("Object Oriented Programming",85)
s1.add_marks("Database Management System",83)
s1.add_marks("Data Structures and Algorithms",80)

s2 = Student("Mehroz",21,"CS-203")
s2.add_marks("Programming Fundamentals",90)
s2.add_marks("Object Oriented Programming",70)
s2.add_marks("Database Management System",80)
s2.add_marks("Data Structures and Algorithms",80)

school.add_student(s1)
school.add_student(s2)

school.save_to_file("school_data.json")
s1.report_card()
school.school_report()