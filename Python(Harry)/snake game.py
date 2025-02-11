while True:
    print("Chose your option(For Computer).")
    print("1. Snake")
    print("2. Water")
    print("3. Gun")
    comp = int(input("Enter your choice: "))
    print("Chose your option(For person).")
    print("1. Snake")
    print("2. Water")
    print("3. Gun")
    per = int(input("Enter your choice: "))

    if comp==per:
        print("It's a Draw.")
    elif comp==1 and per==2:
        print("Computer wins.")
    elif comp==1 and per==3:
        print("Person wins.")
    elif comp==2 and per==1:
        print("Person wins.")
    elif comp==2 and per==3:
        print("Computer wins.")
    elif comp==3 and per==1:
        print("Computer wins.")
    elif comp==3 and per==2:
        print("Person wins.")