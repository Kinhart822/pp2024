import pickle
import threading

def get_user_input(prompt):
    return input(prompt)

def read_students():
    with open('pw8/students.pkl', 'rb') as file:
        return pickle.load(file)

def read_courses():
    with open('pw8/courses.pkl', 'rb') as file:
        return pickle.load(file)

def read_marks():
    with open('pw8/marks.pkl', 'rb') as file:
        return pickle.load(file)

def write_students(students):
    thread = threading.Thread(target=_write_pickle, args=('pw8/students.pkl', students))
    thread.start()

def write_courses(courses):
    thread = threading.Thread(target=_write_pickle, args=('pw8/courses.pkl', courses))
    thread.start()

def write_marks(marks):
    thread = threading.Thread(target=_write_pickle, args=('pw8/marks.pkl', marks))
    thread.start()

def _write_pickle(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)