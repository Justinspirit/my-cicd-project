students = {}

def add_student(system_code, name, course):
    if system_code in students:
        return "System code already exists!"

    students[system_code] = {
        "name": name,
        "course": course
    }
    return "Student added successfully!"

def view_students():
    if not students:
        print("No student records found.")
        return

    for code, student in students.items():
        print(
            f"Code: {code} | "
            f"Name: {student['name']} | "
            f"Course: {student['course']}"
        )

def search_student(system_code):
    return students.get(system_code)

def delete_student(system_code):
    if system_code in students:
        del students[system_code]
        return "Student deleted successfully!"
    return "Student not found."

def main():
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            code = input("Enter system code: ")
            name = input("Enter student name: ")
            course = input("Enter course: ")
            print(add_student(code, name, course))

        elif choice == "2":
            view_students()

        elif choice == "3":
            code = input("Enter system code: ")
            student = search_student(code)
            print(student if student else "Student not found.")

        elif choice == "4":
            code = input("Enter system code: ")
            print(delete_student(code))

        elif choice == "5":
            print("System closed. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
