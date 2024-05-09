phone_number = input("What is your phone number? ")

phone_digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"

}

phone_number_words = ""

for i in phone_number:
    phone_number_words += f"{phone_digits[i]} "

print(phone_number_words)    