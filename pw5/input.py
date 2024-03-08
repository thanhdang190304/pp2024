from input import input_student_info, input_course_info, input_marks

def main():
    check_and_load_data()
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    input_student_info(student_id, student_name, student_dob)
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    input_course_info(course_id, course_name)
    marks = []  
    input_marks(marks)
if __name__ == "__main__":
    main()