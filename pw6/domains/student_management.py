import math
import numpy as np

class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
    def calculate_average_gpa(self, student):
        total_credits = sum(student.credits)
        weighted_sum = np.dot(student.marks, student.credits)
        average_gpa = weighted_sum / total_credits
        return round(average_gpa, 1)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: self.calculate_average_gpa(x), reverse=True)