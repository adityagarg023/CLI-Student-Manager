import argparse
from src.manager import Manager
from src.student import Student
from src.utils import input_int

manager = Manager()


def print_students(students):
    if not students:
        print("⚠ No students found")
        return

    for s in students:
        print(
            f"ID: {s['student_id']} | "
            f"Name: {s['name']} | "
            f"Age: {s['age']} | "
            f"Course: {s['course']}"
        )

def interactive_menu():
    while True:
        print("\n1. Add Student")
        print("2. View All")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Export CSV")
        print("7. Exit")

        choice = input("Choice: ")

        try:
            if choice == "1":
                sid = input("ID: ")
                name = input("Name: ")
                age = input_int("Age: ")
                course = input("Course: ")
                grade = input("Grade: ")
                email = input("Email: ")
                manager.add_student(Student(sid, name, age, grade, course, email))

                print("Added")

            elif choice == "2":
                print_students(manager.get_all_students())

            elif choice == "3":
                sid = input("Enter ID: ")
                student = manager.search_student(sid)
                print(student if student else "Not found")

            elif choice == "4":
                sid = input("ID: ")
                name = input("New name: ")
                age = input_int("New age: ")
                course = input("New course: ")
                print("Updated" if manager.update_student(sid, name, age, grade, course, email) else "Not found")

            elif choice == "5":
                sid = input("ID: ")
                print("Deleted" if manager.delete_student(sid) else "Not found")

            elif choice == "6":
                manager.export_to_csv()
                print("Exported to CSV")

            elif choice == "7":
                break

            else:
                print("Invalid")

        except ValueError as e:
            print(f"{e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--search")
    args = parser.parse_args()

    if args.list:
        print_students(manager.get_all_students())
    elif args.search:
        print(manager.search_student(args.search))
    else:
        interactive_menu()


if __name__ == "__main__":
    main()