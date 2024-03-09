import tkinter as tk
from tkinter import messagebox

from input import PersistenceManager

def submit_student_info():
    student_id = student_id_entry.get()
    student_name = student_name_entry.get()
    student_dob = student_dob_entry.get()
    persistence_manager.input_student_info(student_id, student_name, student_dob)
    messagebox.showinfo("Success", "Student information saved successfully")

def submit_course_info():
    course_id = course_id_entry.get()
    course_name = course_name_entry.get()
    persistence_manager.input_course_info(course_id, course_name)
    messagebox.showinfo("Success", "Course information saved successfully")

persistence_manager = PersistenceManager()

window = tk.Tk()
window.title("Student Course System")


student_id_label = tk.Label(window, text="Student ID:")
student_id_entry = tk.Entry(window)
student_name_label = tk.Label(window, text="Student Name:")
student_name_entry = tk.Entry(window)
student_dob_label = tk.Label(window, text="Student Date of Birth:")
student_dob_entry = tk.Entry(window)
student_submit_button = tk.Button(window, text="Submit", command=submit_student_info)

course_id_label = tk.Label(window, text="Course ID:")
course_id_entry = tk.Entry(window)
course_name_label = tk.Label(window, text="Course Name:")
course_name_entry = tk.Entry(window)
course_submit_button = tk.Button(window, text="Submit", command=submit_course_info)


student_id_label.grid(row=0, column=0, padx=5, pady=5)
student_id_entry.grid(row=0, column=1, padx=5, pady=5)
student_name_label.grid(row=1, column=0, padx=5, pady=5)
student_name_entry.grid(row=1, column=1, padx=5, pady=5)
student_dob_label.grid(row=2, column=0, padx=5, pady=5)
student_dob_entry.grid(row=2, column=1, padx=5, pady=5)
student_submit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

course_id_label.grid(row=4, column=0, padx=5, pady=5)
course_id_entry.grid(row=4, column=1, padx=5, pady=5)
course_name_label.grid(row=5, column=0, padx=5, pady=5)
course_name_entry.grid(row=5, column=1, padx=5, pady=5)
course_submit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()