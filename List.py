
n = input("Enter the text: ")

list = n.split()
sum = 0

for x in list:
    sum = sum + int (x)
    print("Number is: ", x)

print("Sum is: ", sum)

letters = 0
words = 0
digits = 0

text = input("Enter your text: ")

for x in text:
    x = x.lower()

    if 'a' <= x <= 'z':
        letters = letters + 1
    elif '0' <= x <= '9':
        digits = digits + 1
    elif x == ' ':
        words = words + 1

print(letters, words+1, digits)