import sqlite3

DB_FILE = "data/students.db"


class SQLiteStudentManager:

    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                grade TEXT,
                course TEXT,
                email TEXT
            )
        """)
        self.conn.commit()


    def add_student(self, student):
        self.conn.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (student.student_id, student.name, student.age, student.course)
        )
        self.conn.commit()

    def get_all_students(self):
        cur = self.conn.execute("SELECT * FROM students")
        return cur.fetchall()