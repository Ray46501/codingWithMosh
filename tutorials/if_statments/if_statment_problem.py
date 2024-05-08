# Price of house is $1M
# If buyer has good credit
#   Downpayment of 10%
# Otherwise
#   Downpayment of 20%
# Print downpayment

house_price = 1000000
has_good_credit = True

if has_good_credit:
    downpayment = 0.1 * house_price
else:
    downpayment = 0.2 * house_price    

print(f"Your downpayment is ${downpayment}")