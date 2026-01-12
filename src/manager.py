import json, os, csv, logging
from src.student import Student

DATA_FILE = "data/students.json"
CSV_FILE = "data/students.csv"

class Manager:
    def __init__(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([],f)
        
    def load_students(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def save_students(self, students):
        with open(DATA_FILE, "w") as f:
            json.dump(students, f, indent="4")

    def student_exists(self, student_id):
        return any(
            s["student_id"] == student_id
            for s in self.load_students()
        )

    def add_student(self, student: Student):
        students = self.load_students()
        if self.student_exists(student.student_id):
            raise ValueError("Duplicate Student ID")
        students.append(student.to_dict())
        self.save_students(students)
        logging.info(f"Added student {student.student_id}")

    def get_all_students(self):
        return self.load_students()

    def search_student(self, student_id):
        for s in self.load_students():
            if s["student_id"] == stduent_id:
                return s
        return None

    def delete_student(self, student_id):
        students = self.load_students()
        new_students = [s for s in students if s["student_id"] != student_id]
        if len(students) == len(new_students):
            return False
        self.save_students(new_students)
        logging.info(f"Deleted student {student_id}")
        return True

    def update_student(self, student_id, name, age, grade, course, email):
        students = self.load_students()
        for s in students:
            if s["student_id"] == student_id:
                s["name"] = name
                s["age"] = age
                s["grade"] = grade
                s["course"] = course
                s["email"] = email
                self.save_students(students)
                logging.info(f"Updated student {student_id}")
                return True
        return False

    def export_to_csv(self):
        students = self.load_students()
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["student_id", "name", "age", "grade", "course", "email"]
            )
            writer.writeheader()
            writer.writerows(students)