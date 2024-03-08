import gzip
import pickle
import os

def save_data(file_path, data):
    with gzip.open(file_path, "wb") as file:
        pickle.dump(data, file)

def load_data(file_path):
    if os.path.exists(file_path):
        with gzip.open(file_path, "rb") as file:
            data = pickle.load(file)
            return data
    else:
        return None

def input_student_info(student_id, student_name, student_dob):
    student_info = {
        "student_id": student_id,
        "student_name": student_name,
        "student_dob": student_dob
    }
    students = load_data("students.dat") or []
    students.append(student_info)
    save_data("students.dat", students)

def input_course_info(course_id, course_name):
    course_info = {
        "course_id": course_id,
        "course_name": course_name
    }
    courses = load_data("courses.dat") or []
    courses.append(course_info)
    save_data("courses.dat", courses)

def input_marks(marks):
    pass