def find_maximum(numbers, compare):
    max_number = numbers[0]
    
    for number in numbers[1:]:
        if compare(number, max_number):
            max_number = number
    
    return max_number

numbers = [0,1,2,3,4,5]
compare_function = lambda x, y: x > y
maximum_number = find_maximum(numbers, compare_function)
print("Max number is:", maximum_number)
