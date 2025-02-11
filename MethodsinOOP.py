class Employee:
    id = ""
    name = ""
    salary = ""

    def set(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"ID of Employee is {self.id} and his name is {self.name} and salary is {self.salary}")

a = Employee()
a.set(21,'Shifat','200$')
a.display()
print("------------")
print("RECORDED!")
print("------------")

b = Employee()
b.set(26,'Abrar','300$')
b.display()
print("------------")
print("RECORDED!")
print("------------")

c = Employee()
c.set(33,'Walid','600$')
c.display()
print("------------")
print("RECORDED!")
print("------------")
