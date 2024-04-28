# List Comprehension

# sequence of numbers: 0 to 20
numbers = range(0, 21)

# appends `i` to the list
# only if `i % 2` equals 0
even_numbers = [i for i in numbers if i % 2 == 0]

print(even_numbers)
