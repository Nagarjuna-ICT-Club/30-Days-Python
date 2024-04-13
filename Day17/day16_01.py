# Generators

# similar syntax to function
def squares(stop):
    for i in range(1, stop + 1):
        # uses `yield` instead of `return`
        yield i ** 2


for i in squares(5):
    print(i)
