income = int(input("What is you income ($): "))

has_high_income = income >= 100000
has_good_credit = True
has_criminal_record = False

if has_good_credit or has_good_credit and not has_criminal_record:
    print("You are eligible for a loan!")
else:
    print("You are not eligible for a loan!")   