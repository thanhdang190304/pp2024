class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob
        self.marks = {}

    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks

    def display_marks(self, course_id):
        if course_id in self.marks:
            return self.marks[course_id]
        else:
            return "N/A"

    def display_info(self):
        return f"ID: {self.student_id}, Name: {self.student_name}, DoB: {self.student_dob}"