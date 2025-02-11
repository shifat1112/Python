# Define a class representing a Student
class Student:
    # Constructor to initialize student attributes
    def __init__(self, name, roll, age, grade):
        self.name = name  # Assign student name
        self.roll = roll  # Assign student roll number
        self.age = age    # Assign student age
        self.grade = grade  # Assign student grade

    # Method to display student information
    def display_student(self):
        # Print student details
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Age:", self.age)
        print("Grade:", self.grade)
        print("**********")

# Define a class representing a Student Management System
class StudentManagementSystem:
    # Constructor to initialize student list
    def __init__(self):
        self.students = []  # Initialize an empty list to store students

    # Method to add a student to the system
    def add_student(self, student):
        self.students.append(student)  # Add student to the list
        print("Student added successfully!")  # Print success message

    # Method to remove a student from the system
    def remove_student(self, name):
        # Iterate through students in the list
        for x in self.students:
            if x.name == name:  # If student name matches
                self.students.remove(x)  # Remove student from the list
                print("Student removed successfully!")  # Print success message
                return
        print("Student not found.")  # Print message if student not found

    # Method to display all students in the system
    def display_all_students(self):
        if not self.students:  # If there are no students in the list
            print("No students in the system.")  # Print message
        else:
            print("List of Students:\n")  # Print message
            for x in self.students:  # Iterate through students in the list
                x.display_student()  # Display each student's information

    # Method to update student information
    def update_student(self, roll, new_age, new_grade):
        # Iterate through students in the list
        for x in self.students:
            if x.roll == roll:  # If student roll number matches
                x.age = new_age  # Update student age
                x.grade = new_grade  # Update student grade
                print("Student information updated successfully!")  # Print success message
                return
        print("Student not found.")  # Print message if student not found

# Function to start the Student Management System
def main():
    student_system = StudentManagementSystem()  # Create an instance of StudentManagementSystem

    while True:  # Start an infinite loop
        # Print menu options
        print("\n--------------------------------")
        print("\nStudent Management System Menu:")
        print("\n--------------------------------")

        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display All Students")
        print("4. Update Student Information")
        print("5. Exit")

        choice = input("\nEnter your choice: ")  # Prompt user for input
        print()  # Print empty line for spacing

        if choice == "1":  # If user chooses option 1
            # Prompt user to enter student details
            name = input("Enter student name: ")
            roll = input("Enter student roll number: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            new_student = Student(name, roll, age, grade)  # Create a new Student object
            student_system.add_student(new_student)  # Add student to the system
            print("\n--------------------------------")  # Print separator

        elif choice == "2":  # If user chooses option 2
            name = input("Enter the name of student to remove: ")  # Prompt user for student name
            student_system.remove_student(name)  # Remove student from the system
            print("\n--------------------------------")  # Print separator

        elif choice == "3":  # If user chooses option 3
            student_system.display_all_students()  # Display all students in the system
            print("\n--------------------------------")  # Print separator

        elif choice == "4":  # If user chooses option 4
            roll = input("Enter roll number of student to update: ")  # Prompt user for student roll number
            new_age = input("Enter new age: ")  # Prompt user for new age
            new_grade = input("Enter new grade: ")  # Prompt user for new grade
            student_system.update_student(roll, new_age, new_grade)  # Update student information
            print("\n--------------------------------")  # Print separator

        elif choice == "5":  # If user chooses option 5
            print("Exiting...")  # Print exit message
            break  # Exit the loop and end the program

        else:  # If user enters an invalid choice
            print("Invalid choice. Please enter a number between 1 and 5.")  # Print error message

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function to start the program
