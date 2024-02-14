def intersection(list1, list2):
    elements = filter(lambda x: x in list2, list1)
    intersected_list = list(elements)
    return intersected_list

list1 = [1, 2, 3, 4, 5]
list2 = [1,7, 4, 5, 0]
result = intersection(list1, list2)
print("Intersection of of both list is:", result)
