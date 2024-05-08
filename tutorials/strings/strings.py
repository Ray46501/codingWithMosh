course = "Python 'for' Beginners" # Using single quotes inside double quotes so that quotes can be used in strings
email = ''' 

Hello, Hope you are doing well.

This email is an email

Regards, Raiyan

''' # Using tripe quotes to make string across multiple lines
print(course)
print(email)

# Strings are indexed in oythins tarting from zero
print(course[0]) # This will print the first charcter in course which is P
print(course[1]) # Will print second character y
print(course[-1]) # Will print second last character s
print(course[-2]) # Will print last character r
print(course[0:3]) # Will print index 0 to 3 Pyt
print(course[1:]) # Will print ython 'for' Beginners
print(course[:5]) # Will print Pytho

# STring Formatting

first = "John"
last = "Smith"

msg = f"Hi {first} {last}!" # This is a formatted string
print(msg) # Print Hi John Smith!

# String Methods/Functions
print(len(course)) # Print amount of charcter in course including spaces
print(course.upper()) # Print course in all uppercase charcaters
print(course.lower()) # Print course in all lowercase charcaters
print(course.find("P")) # Returns index of charcter p -> 0
print(course.find("Beginners")) # Returns index of startling letter of beginners -> 13
print(course.replace("Beginners", "Absolute Beginners")) # Replaces Beginners with Absolute Beginners
print("Python" in course) # Checks if Python is in course will return True
print("Java" in course) # Checks if Java is in course will return False
print(course.title()) # Titlecases each word in the string
