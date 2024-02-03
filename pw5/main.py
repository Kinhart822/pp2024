from domains.school import School
from input import get_user_input, read_courses, read_marks, read_students
from output import print_students, print_courses, print_marks
import math
from random import random
import zipfile
import os

# Main
school = School()

# Add students
school.add_student("Phạm Hoàng Anh", "22BI13304", "04/11/2004")
school.add_student("Nguyễn Việt Anh", "22BI13039", "04/11/2004")
school.add_student("Nguyễn Hoài Anh", "22BI13021", "01/11/2004")
school.add_student("Lâm Chí Cường", "22BI13068", "03/11/2004")
school.add_student("Vũ Đức Duy", "22BI13127", "01/11/2004")

# Add courses
school.add_course("FD", "Fundamentals of Databases", 3)
school.add_course("SS", "Signal and Systems", 4)
school.add_course("NM", "Numerical Methods", 3)
school.add_course("ADS", "Algorithm and Data Structure", 4)
school.add_course("APP", "Advanced Programming with Python", 3)
school.add_course("OOP", "Object Oriented Programming", 4)

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
print_students(school.students)

print("\nAll courses:\n")
print_courses(school.courses)

courseID = get_user_input("\n Please choose the course that you want to see the result: \n")

# Ensure the courseID is valid
valid_courseIDs = [course.id for course in school.courses]
if courseID not in valid_courseIDs:
    print("Invalid course ID.")
else:
    print_marks(school.get_course(courseID))

# Write data to files
with open('pw5/students.txt', 'w', encoding='utf-8') as file:
    for student in school.students:
        file.write(f"{student.name} - {student.id} - {student.DoB}\n")

with open('pw5/courses.txt', 'w', encoding='utf-8') as file:
    for course in school.courses:
        file.write(f"{course.name} - {course.id} - {course.credits}\n")

with open('pw5/marks.txt', 'w', encoding='utf-8') as file:
    for course in school.courses:
        for studentID, mark in course.marks.items():
            file.write(f"{studentID} - {course.id} - {mark}\n")

# Compress all files into students.dat
with zipfile.ZipFile('pw5/students.dat', 'w') as archive:
    archive.write('pw5/students.txt', 'students.txt')
    archive.write('pw5/courses.txt', 'courses.txt')
    archive.write('pw5/marks.txt', 'marks.txt')
    
# Check if students.dat exists
if os.path.exists('pw5/students.dat'):
    with zipfile.ZipFile('pw5/students.dat', 'r') as archive:
        # Extract files from the archive
        archive.extract('students.txt', 'pw5/')
        archive.extract('courses.txt', 'pw5/')
        archive.extract('marks.txt', 'pw5/')

    # Load data from files
    students = read_students()
    courses = read_courses()
    marks = read_marks()
else:
    # Initialize data if students.dat doesn't exist
    students = []
    courses = []
    marks = {}