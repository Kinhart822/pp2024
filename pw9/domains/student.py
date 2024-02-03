class Student:
    def __init__(self, name, Id, DoB):
        self.name = name
        self.id = Id
        self.DoB = DoB
        self.marks = {}

    def calculate_GPA(self):
        total_credits = sum(course.credits for course in self.marks.keys())
        weighted_sum = sum(course.credits * mark for course, mark in self.marks.items())
        return weighted_sum / total_credits if total_credits else 0
