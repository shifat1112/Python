'''

class Daffodil():
    def __init__(self) -> None:
        print("---------------------------")

    def student(self):
        print("I'm a STUDENT.")
    def teacher(self):
        print("I'm a TEACHER.")

class Hall(Daffodil):
    def __init__(self) -> None:
        super().__init__()
        print("***************")
    def hal(self):
        print("I'm the AUTHORITY.")

s = Daffodil()
s.student()

p = Hall()
p.student()
p.teacher()
p.hal()

'''



n = int(input("Enter your choice: "))

class Shape():
    a = ""
    b = ""
    def __init__(self) -> None:
        print("Shape: ")
        self.a, self.b = map(int, input().split( ))     

if n == 1:
    class Triangle(Shape):
        def area(self):
            A = 0.5 * self.a * self.b
            print("Area of Triangle is: ", A)
    
    t = Triangle()
    t.area()

elif n == 2:
    class Rectangle(Shape):
        def area(self):
            B =  self.a * self.b
            print("Area of Rectangle is: ", B)

    r = Rectangle()
    r.area()
