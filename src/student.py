class Student:
    def __init__(self, student_id, name, age, grade, course, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course
        self.email = email

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "course": self.course,
            "email": self.email
        }