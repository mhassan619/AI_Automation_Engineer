from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @abstractmethod
    def info(self):
        pass


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.__marks = {}
    
    def add_marks(self, subject, marks):
        if not 0 <= marks <= 100:
            print(f" ❌ Invalid Marks! Please enter marks between 0 to 100.")
            return
        if subject in self.__marks:
            print(f" ⚠️  {subject} already exists.")
            return
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
        return None
    
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
s1.add_marks("Math", 85)
s1.add_marks("Physics", 72)
s1.add_marks("OOP", 91)
s1.add_marks("English", 68)

s2 = Student("Ali", 21, "CS-02")
s2.add_marks("Math", 55)
s2.add_marks("Physics", 61)
s2.add_marks("OOP", 70)
s2.add_marks("English", 58)

s3 = Student("Sara", 20, "CS-03")
s3.add_marks("Math", 95)
s3.add_marks("Physics", 88)
s3.add_marks("OOP", 92)
s3.add_marks("English", 90)

school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

s1.report_card()
school.school_report()
print(f"\n{'*'*35}")
top = school.top_student()
print(f" Top Student: {top.name} - {top.average():.1f}%")
print(f"{'='*35}")

# ## for testing
# student = school.find_student("CS-02")
# if student:
#     student.report_card()
# else:
#     print(f"Student not found!")

# s4 = Student("Mohsan",24,"CS-04")
# s4.add_marks("Physics",150)  # gives marks error
# s4.add_marks("Physics",85)
# s4.add_marks("Physics",70)  ## subject duplicate error