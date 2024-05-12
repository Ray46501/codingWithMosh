def find_max(numbers):

    max_num = numbers[0] 

    for num in numbers[1:]: 
        if num > max_num: 
            max_num = num 
            
    return max_num

