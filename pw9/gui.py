# gui.py
import tkinter as tk
from tkinter import messagebox
from domains.school import School
from input import get_user_input, write_students, write_courses, write_marks
from output import print_students, print_courses, print_marks
import math
from random import random
import os
import zipfile

class SchoolGUI:
    def __init__(self, master):
        self.master = master
        master.title("School Management System")

        self.school = School()

        # Add students
        self.school.add_student("Phạm Hoàng Anh", "22BI13304", "04/11/2004")
        self.school.add_student("Nguyễn Việt Anh", "22BI13039", "04/11/2004")
        self.school.add_student("Nguyễn Hoài Anh", "22BI13021", "01/11/2004")
        self.school.add_student("Lâm Chí Cường", "22BI13068", "03/11/2004")
        self.school.add_student("Vũ Đức Duy", "22BI13127", "01/11/2004")

        # Add courses
        self.school.add_course("FD", "Fundamentals of Databases", 3)
        self.school.add_course("SS", "Signal and Systems", 4)
        self.school.add_course("NM", "Numerical Methods", 3)
        self.school.add_course("ADS", "Algorithm and Data Structure", 4)
        self.school.add_course("APP", "Advanced Programming with Python", 3)
        self.school.add_course("OOP", "Object Oriented Programming", 4)

        # Add marks
        for student in self.school.students:
            self.school.add_mark(student.id, "FD", math.floor(random() * 20))
            self.school.add_mark(student.id, "SS", math.floor(random() * 20))
            self.school.add_mark(student.id, "NM", math.floor(random() * 20))
            self.school.add_mark(student.id, "ADS", math.floor(random() * 20))
            self.school.add_mark(student.id, "APP", math.floor(random() * 20))
            self.school.add_mark(student.id, "OOP", math.floor(random() * 20))

        # Create GUI elements
        self.label = tk.Label(master, text="School Management System", font=("Helvetica", 16))
        self.label.pack()

        self.students_button = tk.Button(master, text="List Students", command=self.list_students)
        self.students_button.pack()

        self.courses_button = tk.Button(master, text="List Courses", command=self.list_courses)
        self.courses_button.pack()

        self.choose_course_label = tk.Label(master, text="Choose Course ID:")
        self.choose_course_label.pack()

        self.course_entry = tk.Entry(master)
        self.course_entry.pack()

        self.marks_button = tk.Button(master, text="List Marks", command=self.list_marks)
        self.marks_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.destroy)
        self.quit_button.pack()

    def list_students(self):
        result = []
        for student in self.school.students:
            result.append(f"{student.name} - {student.id} - {student.DoB} - GPA: {student.calculate_GPA():.1f}")
        messagebox.showinfo("List Students", "\n".join(result))

    def list_courses(self):
        result = []
        for course in self.school.courses:
            result.append(f"Course Name: {course.name} - ID: {course.id} - Credits: {course.credits}")
        messagebox.showinfo("List Courses", "\n".join(result))

    def list_marks(self):
        course_id = self.course_entry.get()
        if course_id not in [course.id for course in self.school.courses]:
            messagebox.showerror("Error", "Invalid course ID.")
            return

        result = []
        for course in self.school.courses:
            if course.id == course_id:
                for student_id, mark in course.marks.items():
                    result.append(f"Student {student_id} got {mark:.1f} in {course.name}")
        messagebox.showinfo("List Marks", "\n".join(result))

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolGUI(root)
    root.mainloop()
