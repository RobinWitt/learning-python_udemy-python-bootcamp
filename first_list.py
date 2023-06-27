animals = ["ape", "girafe", "cheetah", "bear", "zebra"]

# print whole array
print(f"Original array: {animals}")

# array with index
print(f"First, Fourth: {animals[0]}, {animals[3]}")  # use index

# last of array
print(f"Last: {animals[-1]}")

# sort array
animals.sort()
print(f"Sorted array: {animals}")

# or use this
animals_sorted = sorted(animals)
print(f"Sorted array 2: {animals_sorted}")

# sort array in reverse order
animals.sort(reverse=True)
print(f"Reverse sorted array: {animals}")

# get length of array
animals_length = len(animals)
print(f"Length of animals array: {animals_length}")

# overwrite single value
animals[3] = "gorilla"
print(f"new value: {animals[3]}")

# empty list
animals_two = []
print(animals_two)

# add element at end of list / append takes only one argument
animals_two.append("elephant")
animals_two.append("turtle")
print(animals_two)

# add element to specific index
animals_two.insert(1, "rhino")
print(animals_two)

# remove last element of list
animals_two.pop()
print(animals_two)

# remove element from specific index
# del animals_two[1] => does not return removed element
animals_two.pop(1)  # => returns removed element
print(animals_two)

# remove the first matching element value
animals_two.remove("elephant")
print(animals_two)
