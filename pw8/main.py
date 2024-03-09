def main():
    student_info = []  
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    student_info.append((student_id, student_name, student_dob))
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    with open("students.txt", "a") as file:
        for student in student_info:
            file.write(f"{student[0]},{student[1]},{student[2]}\n")
    print("Student information written to students.txt:")
    for student in student_info:
        print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}")
    with open("courses.txt", "a") as file:
        file.write(f"{course_id},{course_name}\n")
    print("Course information written to courses.txt:")
    print(f"ID: {course_id}, Name: {course_name}")
if __name__ == "__main__":
    main()