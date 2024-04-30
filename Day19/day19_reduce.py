from functools import reduce

# lambda for adding two numbers
sum = lambda a, b: a + b

numbers = [1, 2, 3, 4, 5]


res = reduce(sum, numbers)

print(res)
