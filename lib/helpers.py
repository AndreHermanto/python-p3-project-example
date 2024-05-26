import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'db'))

from models import Student, Session

def retrieve_students():
    session = Session()
    students = session.query(Student).all()
    if students:
        for student in students:
            print(student)
    else:
        print("No students found.")
    session.close()

def add_student():
    session = Session()
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    try:
        grade = int(grade)
        new_student = Student(name=name, grade=grade)
        session.add(new_student)
        session.commit()
        print(f"Student {name} added successfully.")
    except ValueError:
        print("Invalid grade. Please enter a valid integer.")
    session.close()

def delete_student():
    session = Session()
    name = input("Enter student name to delete: ")
    students = session.query(Student).filter_by(name=name).all()
    if not students:
        print(f"No student found with name {name}.")
    elif len(students) == 1:
        student = students[0]
        session.delete(student)
        session.commit()
        print(f"Student {name} deleted successfully.")
    else:
        print(f"There are {len(students)} students with the name {name}.")
        confirm = input("Do you want to delete all of them? (yes/no): ").strip().lower()
        if confirm == 'yes':
            for student in students:
                session.delete(student)
            session.commit()
            print(f"All students with the name {name} deleted successfully.")
        else:
            print("No students were deleted.")
    session.close()
