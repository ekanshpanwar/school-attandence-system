import mysql.connector
from datetime import datetime

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # Change to your MySQL username
    password="",       # Change to your MySQL password
    database="school_db"
)
cursor = conn.cursor()

# Function to Register a Student
def register_student():
    name = input("Enter student name: ")
    student_class = input("Enter class: ")
    roll_number = input("Enter roll number: ")

    query = "INSERT INTO students (name, class, roll_number) VALUES (%s, %s, %s)"
    values = (name, student_class, roll_number)

    cursor.execute(query, values)
    conn.commit()
    print("Student registered successfully!")

# Function to Mark Attendance
def mark_attendance():
    student_id = input("Enter Student ID: ")
    date = datetime.today().strftime('%Y-%m-%d')
    status = input("Enter status (Present/Absent): ")

    query = "INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)"
    values = (student_id, date, status)

    cursor.execute(query, values)
    conn.commit()
    print("Attendance marked successfully!")

# Function to View Attendance Report
def view_attendance():
    student_id = input("Enter Student ID to view attendance: ")
    
    query = "SELECT date, status FROM attendance WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    records = cursor.fetchall()

    if not records:
        print("No attendance records found.")
        return
    
    print("\nAttendance Report:")
    for row in records:
        print(f"Date: {row[0]}, Status: {row[1]}")

# Menu for the Attendance System
def main():
    while True:
        print("\nSchool Attendance System")
        print("1. Register Student")
        print("2. Mark Attendance")
        print("3. View Attendance Report")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
