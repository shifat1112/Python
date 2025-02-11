class Triangle:
    base = ''
    height = ''

    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height
    def area(self):
            a = float(0.5 * self.base * self.height)
            print("Area of the triangle is: ", a)

t1 = Triangle(10,20)
t1.area()

t2 = Triangle(20,30)
t2.area()