from random import random

studentInformations = {
    "students": [],
    "numberOfStudents": 0,
    "numberOfCourses": 0,
    "courses": []
}

#   Input Functions
def getNumberOfStudent(n:int):
    studentInformations["numberOfStudents"] = n

def getStudentInformation(name:str, Id:str,Dob:str):
    student = {
        "name":name,
        "id":Id,
        "dob":Dob
    }
    studentInformations["students"].append(student)

def getNumberOfCourses(n:int):
    studentInformations["numberOfCourses"] = n

def getCourseInfomation(Id:str,name:str):
    course = {
        "name":name,
        "id":Id,
        "mark": [0]*len(studentInformations["students"])
    }
    studentInformations["courses"].append(course)

def getStudentMark(studentID:str,courseID:str,mark:float):
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
        print(f"{student['name']} - {student['id']} - {student['dob']}")

def listMark(courseID:str):
    for course in studentInformations["courses"]:
        if courseID == course["id"]:
            for i in range(len(studentInformations["students"])):
                print(f"{studentInformations['students'][i]['name']} got {course['mark'][i]:.2f} in {course['name']}")

#   Main
#       Add students
getNumberOfStudent(5)
getStudentInformation("Phạm Hoàng Anh","22BI13304","04/11/2004")
getStudentInformation("Nguyễn Việt Anh","22BI13039","04/8/2004")
getStudentInformation("Nguyễn Hoài Anh","22BI13021","01/10/2004")
getStudentInformation("Lâm Chí Cường","22BI13068","03/11/2004")
getStudentInformation("Vũ Đức Duy","22BI13127","01/11/2004")

#       Add courses
getNumberOfCourses(3)
getCourseInfomation("ADS","Algorithm and Data Structure")
getCourseInfomation("APP","Advanced Programming with Python")
getCourseInfomation("OOP","Object Oriented Programming")

#       Add mark
for student in studentInformations["students"]:
    getStudentMark(student["id"],"ADS",random() * 20)
    getStudentMark(student["id"],"APP",random() * 20)
    getStudentMark(student["id"],"OOP",random() * 20)

#       Listing the information
print("\nAll students in the class:\n")
listStudent()
print("\nAll courses:\n")
listCourses()
print("\nStudent Mark in APP:\n")
listMark("APP")
print("\nStudent Mark in ADS\n")
listMark("ADS")
print("\nStudent Mark in OOP\n")
listMark("OOP")
