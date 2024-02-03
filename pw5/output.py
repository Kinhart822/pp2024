def print_students(students):
    students.sort(key=lambda student: student.calculate_GPA(), reverse=True)
    for student in students:
        print(f"{student.name} - {student.id} - {student.DoB} - GPA: {student.calculate_GPA():.1f}")

def print_courses(courses):
    for course in courses:
        print(f"Course Name: {course.name} - ID: {course.id} - Credits: {course.credits}")

def print_marks(course):
    for studentID, mark in course.marks.items():
        print(f"Student {studentID} got {mark:.1f} in {course.name}")

