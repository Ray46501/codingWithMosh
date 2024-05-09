names = ["Yug", "Jake", "Jack", "James", "Harry"]
print(names[0])
print(names[2:4])
print(names[2:])
print(names[:4])
print(names[0])
names[0] = "Mosh"
print(names)

# 2D Lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1]) # -> 2

for l in matrix:
    for i in l:
        print(i)

# List Methods

numbers = [0,1,2,3,4,5,6,7,8,9,10]   
numbers.append(20)     
numbers.insert(0,9) # First value is index second value is value you want to replace the index with
numbers.remove(5)
# numbers.clear() # Clears List
numbers.pop() # Removes last value in list
numbers.index(7) # Returns index of 7
numbers.sort()
numbers2 = numbers.copy()
numbers.reverse()

print(numbers)
print(numbers2)