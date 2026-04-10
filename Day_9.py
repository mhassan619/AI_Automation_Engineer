## Lets discuss about Exception Handeling
try:
    # the code whose chances be fail
    result = 10/0
except ZeroDivisionError:
    print("Number can not be divided by zero.")
except ValueError:
    print(f"Wrong Value.")
else:
    print("everything is ok!")
finally:
    print("Program Completed.")

## Common Exeptions
try:
    # 1. ValueError
    age = int("hello")  # ❌ Value Error
    # 2. FileNotError
    open("missing.txt") # ❌ FileNotFoundError
    # 3. keyError
    d = {"name":"Hassan"}
    print(d["age"])  # ❌ KeyError
    # 4. IndexError
    list = [1,2,3]
    print(list[10])  # ❌ IndexError
    # 5. TypeError
    result = "5" + 5 # ❌ TypeError 
except:
    print("Program Completed!")

### Upgraded Student Management System with handeling Exceptions
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @abstractmethod
    def info(self):
        pass

# Handle Exceptions 
class InvalidMarksError(Exception):
    def __init__(self, marks):
        super().__init__(f"❌ Marks {marks} invalid! Marks should between 0-100")
class DuplicateSubjectError(Exception):
    def __init__(self, subject):
        super().__init__(f"❌ {subject} already exists!")
class StudentNotFoundError(Exception):
    def __init__(self, roll_no):
        super().__init__(f"❌ Student with Roll No {roll_no} is found!")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.__marks = {}
    
    def add_marks(self, subject, marks):
        if not 0 <= marks <= 100:
            raise InvalidMarksError(marks)
        if subject in self.__marks:
            raise DuplicateSubjectError(subject)
        self.__marks[subject] = marks
        print(f" ✅ {subject}:{marks} added.")
    
    def get_marks(self):
        return self.__marks
    
    def average(self):
        if not self.__marks:
            return 0
        avg = sum(self.__marks.values()) / len(self.__marks)
        return avg
    
    def grade(self):
        avg = self.average()
        if avg >=80:
            return "A"
        elif avg >= 70 and avg <=79:
            return "B"
        elif avg >= 60 and avg <=69:
            return "C"
        elif avg >= 50 and avg <= 59:
            return "D"
        else:
            return "F"
    
    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Roll No: {self.roll_no}")
        print(f"Average: {self.average()}")
        print(f"Grade: {self.grade()}")
    
    def report_card(self):
        print(f"\n{'='*35}")
        print(f"          REPORT CARD")
        print(f"{'='*35}")
        print(f"  Name: {self.name}")
        print(f"  Roll No: {self.roll_no}")
        print(f"  Age: {self._age}")
        print(f"{'-'*35}")
        for subject, marks in self.__marks.items():
            print(f"  {subject}: {marks}/100")
        print(f"{'-'*35}")
        print(f"  Average: {self.average():.1f}%")
        print(f"  Grade: {self.grade()}")
        print(f"{'='*35}")


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.__students = []
    
    def add_student(self, student):
        self.__students.append(student)
    
    def find_student(self, roll_no):
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
    
    def school_report(self):
        print(f"\n{'='*35}")
        print(f"         {self.school_name}")
        print(f"         SCHOOL REPORT")
        print(f"{'='*35}")
        print(f" Total Students: {len(self.__students)}")
        print(f" Top Student: {self.top_student().name} - {self.top_student().average()}")
        print(f"{'-'*35}")
        print(f"      All Enrolled Students")
        print(f"{'-'*35}")
        for student in self.__students:
            print(f" {student.name}'s Average Score: {student.average()}%")


school = School("Al-Hassan Academy")
s1 = Student("Hassan", 20, "CS-01")
try:
    s1.add_marks("Math",150)
except InvalidMarksError as e:
    print(e)
try:
    s1.add_marks("Math",85)
    s1.add_marks("Math",90)
except DuplicateSubjectError as e:
    print(e)
try:
    school.find_student("CS-99")
except StudentNotFoundError as e:
    print(e)