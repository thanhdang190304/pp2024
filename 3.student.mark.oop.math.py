import math
import numpy as np
import curses

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


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name


class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_student_info(self):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth: ")
            student = Student(student_id, student_name, student_dob)
            self.students.append(student)

    def input_course_info(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_student_marks(self):
        course_id = input("Enter the course ID: ")
        for student in self.students:
            marks = float(input(f"Enter marks for student {student.student_name} in course {course_id}: "))
            marks = math.floor(marks * 10) / 10  # Round down to 1 decimal place
            student.add_marks(course_id, marks)

    def calculate_average_gpa(self, student):
        total_credits = sum(student.credits)
        weighted_sum = np.dot(student.marks, student.credits)
        average_gpa = weighted_sum / total_credits
        return round(average_gpa, 1)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: self.calculate_average_gpa(x), reverse=True)

    def display_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Students:\n")
        for student in self.students:
            stdscr.addstr(student.display_info() + "\n")
        stdscr.refresh()

    def run(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        while True:
            stdscr.addstr("--- MENU ---\n")
            stdscr.addstr("1. Type in student information\n")
            stdscr.addstr("2. Type in course information\n")
            stdscr.addstr("3. Type in student marks\n")
            stdscr.addstr("4. List courses\n")
            stdscr.addstr("5. List students\n")
            stdscr.addstr("6. Show student marks for a course\n")
            stdscr.addstr("7. Exit\n")

            stdscr.addstr("Enter your choice: ")
            choice = stdscr.getstr().decode()

            if choice == "1":
                self.input_student_info()
            elif choice == "2":
                self.input_course_info()
            elif choice == "3":
                self.input_student_marks()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.sort_students_by_gpa()
                self.display_students(stdscr)
            elif choice == "6":
                self.show_student_marks()
            elif choice == "7":
                break
            else:
                stdscr.addstr("Wrong input. Please try again.\n")

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()


if __name__ == "__main__":
    student_management = StudentManagement()
    student_management.run()