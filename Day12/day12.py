# lambda

# normal function
def is_positive(a):
    return a > 0


# Equilvalent lambda function
is_pos = lambda a: a > 0


print(is_positive(5))
print(is_pos(5))
