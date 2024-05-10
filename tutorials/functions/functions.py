def greet(): # Defnines function
    print("Hi")
    print("Welcome")

greet() # Calls function


# Functions with parameters

def greet_user(first_name, last_name): # This function takes a parameter
    print(f"Hi {first_name} {last_name}!")
    print("Welcome")

greet_user("Raiyan", "Rahman") # Calls FUnction and passes parameters

# Keyword arguments

greet_user(last_name="Chaudari", first_name="Yug") # Tells python which value to put in which parameter

# Return statment
def square(num): # If this function is called it will not print anythin this function merley returna value
    return num * num

# to print the result we have to do this
print(square(9))
