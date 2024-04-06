def is_odd(n):

    def is_even(x):
        if x % 2 == 0:
            return True
        return False

    if is_even(n):
        return False
    return True


print(is_even(10))
