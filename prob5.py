def exponential_mapping(numbers, n):
    function = map(lambda x: x ** n, numbers)
    return list(function)


numbers = [2, 4, 6, 8]
n = 2
result = exponential_mapping(numbers, n)
print( numbers, " To the power of", n, "is:", result)
