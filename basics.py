import csv
from datetime import date

FILE_NAME = "attendance.csv"


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, "", ""])

    print("Student added successfully.")


def mark_attendance():
    student_id = input("Enter student ID: ")

    today = str(date.today())
    status = input("Present or Absent (P/A): ").upper()

    if status == "P":
        status = "Present"
    elif status == "A":
        status = "Absent"
    else:
        print("Invalid choice.")
        return

    records = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == student_id:
                    row[2] = today
                    row[3] = status

                records.append(row)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(records)

        print("Attendance marked successfully.")

    except FileNotFoundError:
        print("No students found.")


def view_attendance():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            print("\nID\tName\t\tDate\t\tStatus")
            print("-" * 50)

            for row in reader:
                print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}")

    except FileNotFoundError:
        print("No attendance records found.")


while True:

    print("\n===== ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        view_attendance()

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")
