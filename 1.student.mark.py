# Define empty lists to store student and course information
students = []
courses = []

# Function to input student information
def input_student_info():
    num_students = int(input("Enter the number of students in the class: "))
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        students.append({"id": student_id, "name": student_name, "dob": student_dob})

# Function to input course information
def input_course_info():
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append({"id": course_id, "name": course_name})

# Function to select a course and input marks for students
def input_student_marks():
    course_id = input("Enter the course ID: ")
    for student in students:
        marks = int(input("Enter marks for student {} in course {}: ".format(student["name"], course_id)))
        student.setdefault("marks", {})
        student["marks"][course_id] = marks

# Function to list all courses
def list_courses():
    print("Courses:")
    for course in courses:
        print("ID: {}, Name: {}".format(course["id"], course["name"]))

# Function to list all students
def list_students():
    print("Students:")
    for student in students:
        print("ID: {}, Name: {}, DoB: {}".format(student["id"], student["name"], student["dob"]))

# Function to show student marks for a given course
def show_student_marks():
    course_id = input("Enter the course ID: ")
    print("Student marks for course {}:".format(course_id))
    for student in students:
        if "marks" in student and course_id in student["marks"]:
            print("Student: {}, Marks: {}".format(student["name"], student["marks"][course_id]))
        else:
            print("Student: {}, Marks: N/A".format(student["name"]))

# Main program loop
while True:
    print("\n--- MENU ---")
    print("1. Input student information")
    print("2. Input course information")
    print("3. Input student marks")
    print("4. List courses")
    print("5. List students")
    print("6. Show student marks for a course")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        input_student_info()
    elif choice == "2":
        input_course_info()
    elif choice == "3":
        input_student_marks()
    elif choice == "4":
        list_courses()
    elif choice == "5":
        list_students()
    elif choice == "6":
        show_student_marks()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")