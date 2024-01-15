from random import random

class Student:
    def __init__(self, name, Id, DoB):
        self.name = name
        self.id = Id
        self.DoB = DoB

class Course:
    def __init__(self, Id, name):
        self.id = Id
        self.name = name
        self.marks = {}

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, Id, DoB):
        self.students.append(Student(name, Id, DoB))

    def add_course(self, Id, name):
        self.courses.append(Course(Id, name))

    def add_mark(self, studentID, courseID, mark):
        for course in self.courses:
            if course.id == courseID:
                for student in self.students:
                    if student.id == studentID:
                        course.marks[studentID] = mark

    def list_students(self):
        for student in self.students:
            print(f"{student.name} - {student.id} - {student.DoB}")

    def list_courses(self):
        for course in self.courses:
            print(f"Course Name: {course.name} - ID: {course.id}")

    def list_marks(self, courseID):
        for course in self.courses:
            if course.id == courseID:
                for studentID, mark in course.marks.items():
                    print(f"Student {studentID} got {mark:.2f} in {course.name}")

# Main
school = School()

# Add students
school.add_student("Phạm Hoàng Anh","22BI13304","04/11/2004")
school.add_student("Nguyễn Việt Anh","22BI13039","04/11/2004")
school.add_student("Nguyễn Hoài Anh","22BI13021","01/11/2004")
school.add_student("Lâm Chí Cường","22BI13068","03/11/2004")
school.add_student("Vũ Đức Duy","22BI13127","01/11/2004")

# Add courses
school.add_course("FD","Fundamentals of Databases")
school.add_course("SS","Signal and Systems")
school.add_course("NM","Numerical Methods")
school.add_course("ADS","Algorithm and Data Structure")
school.add_course("APP","Advanced Programming with Python")
school.add_course("OOP","Object Oriented Programming")

# Add marks
for student in school.students:
    school.add_mark(student.id, "FD", random() * 20)
    school.add_mark(student.id, "SS", random() * 20)
    school.add_mark(student.id, "NM", random() * 20)
    school.add_mark(student.id, "ADS", random() * 20)
    school.add_mark(student.id, "APP", random() * 20)
    school.add_mark(student.id, "OOP", random() * 20)

# List the information
print("\nAll students in the class:\n")
school.list_students()
print("\nAll courses:\n")
school.list_courses()
courseID = input("\n Please choose the course that you want to see the result: \n")
school.list_marks(courseID)
