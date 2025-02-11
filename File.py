file = open("File.txt", "r+")

text = file.read()

print(text)
length = len(text)
print(length)


#text = file.readlines()[1]
#for line in file:
 #   print(line)
#print(text)

file.close()


file = open("File.txt", "a")

file.write("\n5. Safiul Islam - 3.65")
file.close()