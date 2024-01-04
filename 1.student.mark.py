from random import random

studentInformations = {
    "students": [],
    "numberOfStudents": 0,
    "numberOfCourses": 0,
    "courses": []
}

#   Input Functions
def numberOfStudent(n:int):
    studentInformations["numberOfStudents"] = n

def informations(name:str, Id:str,DoB:str):
    student = {
        "name":name,
        "id":Id,
        "DoB":DoB
    }
    studentInformations["students"].append(student)

def numberOfCourses(n:int):
    studentInformations["numberOfCourses"] = n

def courseInfomations(Id:str,name:str):
    course = {
        "name":name,
        "id":Id,
        "mark": [0]*len(studentInformations["students"])
    }
    studentInformations["courses"].append(course)

def studentMark(studentID:str,courseID:str,mark:float):
    index = 0
    for student in studentInformations["students"]:
        if student["id"] == studentID:
            break
        index += 1

    for course in studentInformations["courses"]:
        if course["id"] == courseID:
            course["mark"][index] = mark

#   Listing Functions
def listCourses():
    for course in studentInformations["courses"]:
        print(f"Course Name: {course['name']} - ID: {course['id']}")

def listStudent():
    for student in studentInformations["students"]:
        print(f"{student['name']} - {student['id']} - {student['DoB']}")

def listMark(courseID:str):
    for course in studentInformations["courses"]:
        if courseID == course["id"]:
            for i in range(len(studentInformations["students"])):
                print(f"{studentInformations['students'][i]['name']} got {course['mark'][i]:.2f} in {course['name']}")

#   Main
#       Add students
numberOfStudent(5)
informations("Phạm Hoàng Anh","22BI13304","04/11/2004")
informations("Nguyễn Việt Anh","22BI13039","04/11/2004")
informations("Nguyễn Hoài Anh","22BI13021","01/11/2004")
informations("Lâm Chí Cường","22BI13068","03/11/2004")
informations("Vũ Đức Duy","22BI13127","01/11/2004")

#       Add courses
numberOfCourses(3)
courseInfomations("ADS","Algorithm and Data Structure")
courseInfomations("AP","Advanced Programming with Python")
courseInfomations("OOP","Object Oriented Programming")

#       Add mark
for student in studentInformations["students"]:
    studentMark(student["id"],"ADS",random() * 20)
    studentMark(student["id"],"AP",random() * 20)
    studentMark(student["id"],"OOP",random() * 20)

#       Listing the information
print("\nAll students in the class:\n")
listStudent()
print("\nAll courses:\n")
listCourses()
print("\nStudent Mark in APP:\n")
listMark("AP")
print("\nStudent Mark in ADS\n")
listMark("ADS")
print("\nStudent Mark in OOP\n")
listMark("OOP")
