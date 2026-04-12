# To see current Branch
# git branch

# To make new branch
# git branch feature-login

# Go to that branch
# git checkout feature-login

# Shortcut - To make and go to same in one command
# git checkout -b feature-login

# after working - do commit
# git add .
# git commit -m "Login feature added."

# Come back to main branch
# git checkout main

# To merge
# git merge feature-login

# Delete the branch - work is done
# git branch -d feature-login

# Merge Conflict 
# When same file edits from two same places in two branches - then git confuses
# <<<<<<<< Head
# print("Main branch Code")
# =======
# print("Feature Branch Code")
# >>>>>>>> feature-login

# You have to decide which code you want to keep
# Then:
# git add .
# git commit -m "Conflict Resolved."

from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self._age = age
    @abstractmethod
    def info(self):
        pass
class InvalidMarksError(Exception):
    def __init__(self, marks):
        super().__init__(f"Marks {marks} invalid! Please enter marks between 1 to 100!")
class DuplicateSubjectError(Exception):
    def __init__(self, subject):
        super().__init__(f"Subject {subject} already exists!")
class StudentNotFoundError(Exception):
    def __init__(self, roll_no):
        super().__init__(f"Student with roll_no {roll_no} is not found!")
class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.__marks = {}
    def add_marks(self,subject,marks):
        if not 0 <= marks <= 100:
            raise InvalidMarksError(marks)
        if subject in self.__marks:
            raise DuplicateSubjectError(subject)
        self.__marks[subject] = marks
    def get_marks(self):
        return self.__marks
    def average(self):
        avg = sum(self.__marks.values())/ len(self.__marks)
        return avg
    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif 70 <= avg <= 79:
            return "B"
        elif 60 <= avg <= 69:
            return "C"
        elif 50 <= avg <= 59:
            return "D"
        else:
            return "F"
    def info(self):
        print(f"Name:{self.name}")
        print(f"Age:{self._age}")
        print(f"Roll No:{self.roll_no}")
        print(f"Grade:{self.grade()}")
        print(f"Average:{self.average():.1f}%")
    def report_card(self):
        print(f"\n{'='*35}")
        print(f"        REPORT CARD")
        print(f"{'='*35}")
        print(f"  Name:{self.name}")
        print(f"  Roll No:{self.roll_no}")
        print(f"  Age:{self._age}")
        print(f"{'-'*35}")
        for subject,marks in self.__marks.items():
            print(f"  {subject}:{marks}/100")
        print(f"{'-'*35}")
        print(f"  Grade:{self.grade()}")
        print(f"  Average:{self.average():.1f}%")
        print(f"{'='*35}")
class School:
    def __init__(self,school_name):
        self.school_name = school_name
        self.__students = []
    def add_student(self,student):
        self.__students.append(student)
    def find_student(self,roll_no):
        for student in self.__students:
            if student.roll_no == roll_no:
                return student
        raise StudentNotFoundError(roll_no)
    def top_student(self):
        return max(self.__students, key=lambda s: s.average())
    def all_students(self):
        if not self.__students:
            print(f"There are no students yet.")
        for student in self.__students:
            print(f"{student.info()}")
    def failed_students(self):
        for student in self.__students:
            if student.average() < 50:
                yield student
    def topper_certificate(self):
        top = self.top_student()
        print(f"""
        CERTIFICATE OF MERIT
    {top.name:<32}||
    Grade: {top.grade():<27} ||
    Average: {top.average():.1f}%{' '*21} ||
""")
    def school_report(self):
        print(f"\n{'='*35}")
        print(f"      {self.school_name}")
        print(f"        SCHOOL REPORT")
        print(f"{'='*35}")
        print(f"Total Students:{len(self.__students)}")
        print(f"Top Student:{self.top_student().name} - {self.top_student().average():.1f}%")
        print(f"{'-'*35}")
        print(f"  ALL ENROLLED STUDENTS")
        print(f"{'-'*35}")
        for student in self.__students:
            print(f"{student.name} - {student.average():.1f}%")
school = School("Al-Hassan Academy")

s1 = Student("Hassan",21,"CS-101")
s2 = Student("Mehroz Gul",22,"CS-102")
s3 = Student("Safi Ullah",23,"CS-103")

s1.add_marks("PF",95)
s1.add_marks("OOP",85)
s1.add_marks("DSA",80)
s1.add_marks("DBMS",83)

s2.add_marks("PF",90)
s2.add_marks("OOP",70)
s2.add_marks("DSA",80)
s2.add_marks("DBMS",80)

s3.add_marks("PF",93)
s3.add_marks("OOP",73)
s3.add_marks("DSA",80)
s3.add_marks("DBMS",80)

school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

s1.report_card()
school.school_report()