ch = []

i=1
while i<6:
    ch[i] = str(input("Enter a character: "))
    i = i + 1

print("The characters are: ", end='')
i=1
while i<6:
    print(ch[i])
    i = i + 1

ch.sort()

print("The characters are: ", end='')
i=1
while i<6:
    print(ch[i])
    i = i + 1