from domains.school import School
from input import get_user_input
from output import print_students, print_courses, print_marks
import math
from random import random

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
