# This function prints if the given
# parameter 'n' is even or odd
def is_even_or_odd(n):
    if n % 2 == 0:
        print(f'{n} is even.')
    else:
        print(f'{n} is odd.')


# Function should be called for it to run
is_even_or_odd(10)
is_even_or_odd(5)


# The previous function didnot return anything
# 'return' statement is used to return data from a function
def greater(a, b):
    if a > b:
        return a
    else:
        return b


# 'greater' returns a value which is greater than the other
a = greater(10, 5)
print(a)
