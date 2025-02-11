class Student:
    id = 5214
    name = "Shifat"
    cgpa = 3.79

    def info(self):
        print(f"{self.name} whose id is {self.id} and cgpa is {self.cgpa}")

a = Student()
a.name = "Abrar"
a.id = 5053
a.cgpa = 3.83
a.info()

b = Student()
b.name = "Walid"
b.id = 5054
b.cgpa = 3.72
b.info()

c = Student()
c.info()