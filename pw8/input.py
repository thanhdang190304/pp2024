import gzip
import pickle
import os
import threading

class PersistenceManager:
    def __init__(self):
        self.students_file = "students.dat"
        self.courses_file = "courses.dat"
        self.students_lock = threading.Lock()
        self.courses_lock = threading.Lock()

    def save_data(self, file_path, data):
        with gzip.open(file_path, "wb") as file:
            pickle.dump(data, file)

    def load_data(self, file_path):
        if os.path.exists(file_path):
            with gzip.open(file_path, "rb") as file:
                data = pickle.load(file)
                return data
        else:
            return None

    def save_students_data(self, students):
        with self.students_lock:
            threading.Thread(target=self.save_data, args=(self.students_file, students)).start()

    def save_courses_data(self, courses):
        with self.courses_lock:
            threading.Thread(target=self.save_data, args=(self.courses_file, courses)).start()

    def input_student_info(self, student_id, student_name, student_dob):
        student_info = {
            "student_id": student_id,
            "student_name": student_name,
            "student_dob": student_dob
        }
        students = self.load_data(self.students_file) or []
        students.append(student_info)
        self.save_students_data(students)

    def input_course_info(self, course_id, course_name):
        course_info = {
            "course_id": course_id,
            "course_name": course_name
        }
        courses = self.load_data(self.courses_file) or []
        courses.append(course_info)
        self.save_courses_data(courses)

    def input_marks(self, marks):
        # Add your implementation to handle inputting marks here
        pass

def main():
    persistence_manager = PersistenceManager()
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    persistence_manager.input_student_info(student_id, student_name, student_dob)
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    persistence_manager.input_course_info(course_id, course_name)
    print("Student information written to students.dat:")
    print(f"ID: {student_id}, Name: {student_name}, DOB: {student_dob}")
    print("Course information written to courses.dat:")
    print(f"ID: {course_id}, Name: {course_name}")

if __name__ == "__main__":
    main()