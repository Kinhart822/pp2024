from random import random

class Student:
    def __init__(self, name, Id, Dob):
        self.name = name
        self.id = Id
        self.dob = Dob

class Course:
    def __init__(self, Id, name):
        self.name = name
        self.id = Id
        self.marks = {}

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, Id, Dob):
        self.students.append(Student(name, Id, Dob))

    def add_course(self, Id, name):
        self.courses.append(Course(Id, name))

    def get_student_mark(self, studentID, courseID, mark):
        for course in self.courses:
            if course.id == courseID:
                for student in self.students:
                    if student.id == studentID:
                        course.marks[studentID] = mark

    def list_courses(self):
        for course in self.courses:
            print(f"Course Name: {course.name} - ID: {course.id}")

    def list_students(self):
        for student in self.students:
            print(f"{student.name} - {student.id} - {student.dob}")

    def list_marks(self, courseID):
        for course in self.courses:
            if course.id == courseID:
                for studentID, mark in course.marks.items():
                    for student in self.students:
                        if student.id == studentID:
                            print(f"{student.name} got {mark:.2f} in {course.name}")

# Main
school = School()

# Add students
school.add_student("Phạm Hoàng Anh","22BI13304","04/11/2004")
school.add_student("Nguyễn Việt Anh","22BI13039","04/11/2004")
school.add_student("Nguyễn Hoài Anh","22BI13021","01/11/2004")
school.add_student("Lâm Chí Cường","22BI13068","03/11/2004")
school.add_student("Vũ Đức Duy","22BI13127","01/11/2004")

# Add courses
school.add_course("ADS","Algorithm and Data Structure")
school.add_course("APP","Advanced Programming with Python")
school.add_course("OOP","Object Oriented Programming")

# Add marks
for student in school.students:
    school.get_student_mark(student.id, "ADS", random() * 20)
    school.get_student_mark(student.id, "APP", random() * 20)
    school.get_student_mark(student.id, "OOP", random() * 20)

# List the information
print("\nAll students in the class:\n")
school.list_students()
print("\nAll courses:\n")
school.list_courses()
print("\nStudent Mark in APP:\n")
school.list_marks("APP")
print("\nStudent Mark in ADS\n")
school.list_marks("ADS")
print("\nStudent Mark in OOP\n")
school.list_marks("OOP")
