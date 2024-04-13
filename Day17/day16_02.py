# Generators

# change string to uppercase
# and yield one at a time
def modify(strings):
    for s in strings:
        yield s.upper()


units = ['mg', 'g', 'kg']
for i in modify(units):
    print(i)
