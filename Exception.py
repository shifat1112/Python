try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    result = a/b
    print(result)
    print("Done.")

except ValueError:
    print("Enter correct value.")
except ZeroDivisionError:
    print("Can't be devided by 0")
finally:
    print("Succesful.")
