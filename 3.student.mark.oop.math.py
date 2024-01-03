import math
import numpy as np
import curses
import random  

class Student:
    def __init__(self, name, Id, Dob):
        self.name = name
        self.id = Id
        self.dob = Dob
        self.marks = {}
        self.gpa = 0

class Course:
    def __init__(self, Id, name, credits):
        self.name = name
        self.id = Id
        self.credits = credits
        self.marks = {}

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, Id, Dob):
        self.students.append(Student(name, Id, Dob))

    def add_course(self, Id, name, credits):
        self.courses.append(Course(Id, name, credits))

    def get_student_mark(self, studentID, courseID, mark):
        mark = math.floor(mark * 10) / 10
        for course in self.courses:
            if course.id == courseID:
                for student in self.students:
                    if student.id == studentID:
                        course.marks[studentID] = mark
                        student.marks[courseID] = mark

    def calculate_gpa(self, studentID):
        marks = []
        credits = []
        for course in self.courses:
            if studentID in course.marks:
                marks.append(course.marks[studentID])
                credits.append(course.credits)
        marks = np.array(marks)
        credits = np.array(credits)
        gpa = np.sum(marks * credits) / np.sum(credits)
        for student in self.students:
            if student.id == studentID:
                student.gpa = gpa

    def sort_students(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)

    def list_students(self):
        for student in self.students:
            print(f"{student.name} - {student.id} - {student.dob} - GPA: {student.gpa:.1f}")

# Main
school = School()

# Add students
school.add_student("Phạm Hoàng Anh","22BI13304","04/11/2004")
school.add_student("Nguyễn Việt Anh","22BI13039","04/8/2004")
school.add_student("Nguyễn Hoài Anh","22BI13021","01/10/2004")
school.add_student("Lâm Chí Cường","22BI13068","03/11/2004")
school.add_student("Vũ Đức Duy","22BI13127","01/11/2004")

# Add courses
school.add_course("ADS","Algorithm and Data Structure", 3)
school.add_course("APP","Advanced Programming with Python", 3)
school.add_course("OOP","Object Oriented Programming", 3)

# Add marks
for student in school.students:
    school.get_student_mark(student.id, "ADS", random.random() * 20)  
    school.get_student_mark(student.id, "APP", random.random() * 20)  
    school.get_student_mark(student.id, "OOP", random.random() * 20)  

# Calculate GPA
for student in school.students:
    school.calculate_gpa(student.id)

# Sort students by GPA
school.sort_students()

# List the students
school.list_students()
