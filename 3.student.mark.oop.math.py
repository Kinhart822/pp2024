import math
import numpy as np
import curses
from random import random


class Student:
    def __init__(self, name, Id, DoB):
        self.name = name
        self.id = Id
        self.DoB = DoB
        self.marks = {}

    def calculate_GPA(self):
        total_credits = sum(course.credits for course in self.marks.keys())
        weighted_sum = sum(course.credits * mark for course, mark in self.marks.items())
        return weighted_sum / total_credits if total_credits else 0

class Course:
    def __init__(self, Id, name, credits):
        self.id = Id
        self.name = name
        self.credits = credits
        self.marks = {}

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, Id, DoB):
        self.students.append(Student(name, Id, DoB))

    def add_course(self, Id, name, credits):
        self.courses.append(Course(Id, name, credits))

    def add_mark(self, studentID, courseID, mark):
        for course in self.courses:
            if course.id == courseID:
                for student in self.students:
                    if student.id == studentID:
                        course.marks[studentID] = mark
                        student.marks[course] = mark

    def list_students(self):
        self.students.sort(key=lambda student: student.calculate_GPA(), reverse=True)
        for student in self.students:
            print(f"{student.name} - {student.id} - {student.DoB} - GPA: {student.calculate_GPA():.1f}")

    def list_courses(self):
        for course in self.courses:
            print(f"Course Name: {course.name} - ID: {course.id} - Credits: {course.credits}")

    def list_marks(self, courseID):
        for course in self.courses:
            if course.id == courseID:
                for studentID, mark in course.marks.items():
                    print(f"Student {studentID} got {mark:.1f} in {course.name}")

# Main
school = School()

# Add students
school.add_student("Phạm Hoàng Anh","22BI13304","04/11/2004")
school.add_student("Nguyễn Việt Anh","22BI13039","04/11/2004")
school.add_student("Nguyễn Hoài Anh","22BI13021","01/11/2004")
school.add_student("Lâm Chí Cường","22BI13068","03/11/2004")
school.add_student("Vũ Đức Duy","22BI13127","01/11/2004")

# Add courses
school.add_course("FD","Fundamentals of Databases", 3)
school.add_course("SS","Signal and Systems", 4)
school.add_course("NM","Numerical Methods", 3)
school.add_course("ADS","Algorithm and Data Structure", 4)
school.add_course("APP","Advanced Programming with Python", 3)
school.add_course("OOP","Object Oriented Programming", 4)

# Add marks
for student in school.students:
    school.add_mark(student.id, "FD", math.floor(random() * 20))
    school.add_mark(student.id, "SS", math.floor(random() * 20))
    school.add_mark(student.id, "NM", math.floor(random() * 20))
    school.add_mark(student.id, "ADS", math.floor(random() * 20))
    school.add_mark(student.id, "APP", math.floor(random() * 20))
    school.add_mark(student.id, "OOP", math.floor(random() * 20))

# List the information
print("\nAll students in the class:\n")
school.list_students()
print("\nAll courses:\n")
school.list_courses()
courseID = input("\n Please choose the course that you want to see the result: \n")
school.list_marks(courseID)
