# Write program to find largest number in a list

numbers = [0,1,2,3,4,5,6,7,8,19,10]
largest_num = 0

for num in numbers:
    if num > largest_num:
        largest_num = num

print(f"The largest number in the list is {largest_num}")