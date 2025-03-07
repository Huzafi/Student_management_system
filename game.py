import csv
from google.colab import files

def student_management_system():
    """
    A simple student management system that allows for adding, viewing, and saving student data to a CSV file.
    """

    def add_student(students):
        """Adds a new student to the student list."""
        name = input("Enter student name: ")
        roll_number = input("Enter student roll number: ")
        grade = input("Enter student grade: ")
        students.append([name, roll_number, grade])
        print(f"Student {name} added successfully!")

    def view_students(students):
      """Displays the list of students."""
      if not students:
          print("No students in the database yet.")
          return

      print("-" * 30)
      print("{:<15} {:<15} {:<10}".format("Name", "Roll Number", "Grade"))
      print("-" * 30)
      for student in students:
          print("{:<15} {:<15} {:<10}".format(student[0], student[1], student[2]))
      print("-" * 30)


    def save_students_to_csv(students, filename="students.csv"):
        """Saves the student data to a CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Roll Number", "Grade"])  # Write header row
            writer.writerows(students)
        print(f"Student data saved to {filename}")


    students = []
    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save to CSV")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            save_students_to_csv(students)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

student_management_system()

