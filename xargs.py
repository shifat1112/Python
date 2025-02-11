def id(*num):
    y = num[0]
    print("First number:", y)
    print("Total numbers:", len(num))
    sub = 0  # Initialize sub outside the loop
    for x in range(1, len(num)):  # Adjust the range to start from 1
        y = y - num[x]  # Fix the subtraction operation
    print("Subtraction:", y)

id(20,10)
id(60,43,65)
id(1001,565,76,23,76)
