# import specific functions from a module
from itertools import cycle

data = ['python', 'is', 'amazing']

# cycle() iterates over the given
# iterable indefinitely
for i in cycle(data):
    print(i)
