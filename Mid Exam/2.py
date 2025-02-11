def chat(a):
    if a == "Hi!":
        print("Hi! What can I do now?")
    elif a == "Do you know me?":
        print("You are from DIU.")
    elif a == "Thanks for your information.":
        print("Thanks.")
    else:
        print("Sorry! I don't understand you.")

while True:
    n = str(input("You: "))
    if n == 'bye':
        break
    chat(n)
