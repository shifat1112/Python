from random import randint

for x in range(5):
    a = int(input("Enter your guessing number: "))

    rand = randint(1,5) 

    if a == rand:
        print("You have won.")
    else:
        print("You have lost.")
        print("The random number was: ", rand)