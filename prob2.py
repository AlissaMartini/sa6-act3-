list = ["Awesome", "Bear", "Car", "Deer", "Elephant", "Peach"]
sorted_list = sorted(list, key=lambda x: (len(x), x))

print("Sorted list of strings:", sorted_list)
