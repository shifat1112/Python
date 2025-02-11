class student:

    def __init__(self, name, id, cgpa):

        self.name = name
        self.id = id
        self.cgpa = cgpa
    
    def info(self):
        print(f"{self.name}'s id is {self.id} and cgpa is {self.cgpa}")

a = student("Shifat", 5214, 3.78)
a.info()
b = student("Abrar", 5053, 3.83)
b.info()        
c = student("Walid", 5054, 3.67)
c.info()