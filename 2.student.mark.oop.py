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
            marks = int(input(f"Enter marks for student {student.student_name} in course {course_id}: "))
            student.add_marks(course_id, marks)

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.course_name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(student.display_info())

    def show_student_marks(self):
        course_id = input("Enter the course ID: ")
        print(f"Student marks for course {course_id}:")
        for student in self.students:
            marks = student.display_marks(course_id)
            print(f"Student: {student.student_name}, Marks: {marks}")

    def run(self):
        while True:
            print("\n--- MENU ---")
            print("1. Type in student information")
            print("2. Type in course information")
            print("3. Type in student marks")
            print("4. List courses")
            print("5. List students")
            print("6. Show student marks for a course")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.input_student_info()
            elif choice == "2":
                self.input_course_info()
            elif choice == "3":
                self.input_student_marks()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.list_students()
            elif choice == "6":
                self.show_student_marks()
            elif choice == "7":
                break
            else:
                print("Wrong input. Please try again.")


