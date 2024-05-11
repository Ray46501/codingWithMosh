while True:
    try: # Initiantes try and except code block
        age = int(input("Age: "))
        income = 20000
        risk = income / age

        print(f"You are {age} years old")
        break
    except ZeroDivisionError:
        print("Age cannot be zero!")    
    except ValueError:
        print("Invalid Input!")    