while True:
    name = input("What is your name? ")

    if len(name) < 3:
        print("Name must be longer than 3 charcter! ")
    elif len(name) > 50:
        print("Name must less than 50 characters! ")   
    else:
        print(f"Your name is {name}!")