
student = {
    101 : "Shifat Ahmed",
    102 : "Abrar Javed",
    103 : "Walid Yousuf",
    
}
for i in range(5):
    n = int(input("Enter a key number: "))

    print("The key value is: ", student.get(n, "Not Available"))