ch = str(input("Enter a character: "))

if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
    if ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='u' or ch=='U':
        print("It is a Vowel.")
    else:
        print("It is a consonant.")

else:
    print("Enter valid character.")