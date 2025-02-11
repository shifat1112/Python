class Student:
    def __init__(self, name, roll, age, grade):
        self.name = name
        self.roll = roll
        self.age = age
        self.grade = grade

    def display_student(self):
        
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Age:", self.age)
        print("Grade:", self.grade)
        print("**********")

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def remove_student(self, name):
        for x in self.students:
            if x.name == name:
                self.students.remove(x)
                print("Student removed successfully!")
                return
        print("Student not found.")

    def display_all_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("List of Students:\n")
            for x in self.students:
                x.display_student()

    def search_student(self, name):
        for student in self.students:
            if student.name == name:
                student.display_student()
                return
        print("Student not found.")

    def update_student(self, roll, new_age, new_grade):
        for x in self.students:
            if x.roll == roll:
                x.age = new_age
                x.grade = new_grade
                print("Student information updated successfully!")
                return
        print("Student not found.")

def main():
    student_system = StudentManagementSystem()

    while True:
        print("\n--------------------------------")
        print("\nStudent Management System Menu:")
        print("\n--------------------------------")

        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display All Students")
        print("4. Update Student Information")
        print("5. Search Student")
        print("6. Exit")

        choice = input("\nEnter your choice: ")
        print()

        if choice == "1":
            name = input("Enter student name: ")
            roll = input("Enter student roll number: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            new_student = Student(name, roll, age, grade)
            student_system.add_student(new_student)
            print("\n--------------------------------")

        elif choice == "2":
            name = input("Enter the name of student to remove: ")
            student_system.remove_student(name)
            print("\n--------------------------------")

        elif choice == "3":
            student_system.display_all_students()
            print("\n--------------------------------")

        elif choice == "4":
            roll = input("Enter roll number of student to update: ")
            new_age = input("Enter new age: ")
            new_grade = input("Enter new grade: ")
            student_system.update_student(roll, new_age, new_grade)
            print("\n--------------------------------")
        
        elif choice == "5":
            name = input("Enter the name of student to search: ")
            student_system.search_student(name)
            print("\n--------------------------------")

        elif choice == "6":
            print("Thank you for using the Student Management System!\nExiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


