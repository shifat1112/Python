class Employee:
    def __init__(self) -> None:
        id = ""
        name = ""
        salary = ""

n = 2#input(int("Enter the numbers of Employee: "))
Employees = []
for i in range (1,n+1):
    em = Employee()
    em.id = input("Enter the id: ")
    em.name = input("Enter the name: ")
    em.salary = input("Enter the salary: ")
    Employees.append(em)
    print("Recorded")
    print()
    print()
for i,em in enumerate(Employees):
    print(f"ID of Employee {i+1} is {em.id} and his name is {em.name} and salary is {em.salary}")