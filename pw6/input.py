import pickle

def get_user_input(prompt):
    return input(prompt)

def read_students():
    with open('pw6/students.pkl', 'rb') as file:
        return pickle.load(file)

def read_courses():
    with open('pw6/courses.pkl', 'rb') as file:
        return pickle.load(file)

def read_marks():
    with open('pw6/marks.pkl', 'rb') as file:
        return pickle.load(file)

def write_students(students):
    with open('pw6/students.pkl', 'wb') as file:
        pickle.dump(students, file)

def write_courses(courses):
    with open('pw6/courses.pkl', 'wb') as file:
        pickle.dump(courses, file)

def write_marks(marks):
    with open('pw6/marks.pkl', 'wb') as file:
        pickle.dump(marks, file)