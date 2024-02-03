from domains.student import Student
from domains.course import Course

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
        
    def get_course(self, courseID):
        for course in self.courses:
            if course.id == courseID:
                return course
