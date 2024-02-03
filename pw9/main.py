from domains.school import School
from input import get_user_input, read_courses, read_marks, read_students, write_courses, write_marks, write_students
from output import print_students, print_courses, print_marks
import math
from random import random
import zipfile
import pickle
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

# Write data to files using pickle in a background thread
write_students(school.students)
write_courses(school.courses)
write_marks({course.id: course.marks for course in school.courses})

# Compress all files into students.dat using pickle
with zipfile.ZipFile('pw8/students.dat', 'w') as archive:
    archive.write('pw8/students.pkl', 'students.pkl')
    archive.write('pw8/courses.pkl', 'courses.pkl')
    archive.write('pw8/marks.pkl', 'marks.pkl')

# Check if students.dat exists
if os.path.exists('pw8/students.dat'):
    with zipfile.ZipFile('pw8/students.dat', 'r') as archive:
        # Extract files from the archive
        archive.extract('students.pkl', 'pw8/')
        archive.extract('courses.pkl', 'pw8/')
        archive.extract('marks.pkl', 'pw8/')

    # Load data from files using pickle
    students = read_students()
    courses = read_courses()
    marks = read_marks()
else:
    # Initialize data if students.dat doesn't exist
    students = []
    courses = []
    marks = {}

# Replace existing code that uses txt files with the new data structures
school.students = students
school.courses = courses
for course in school.courses:
    course.marks = marks.get(course.id, {})