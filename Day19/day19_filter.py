def is_number(x):
    num_types = (int, float)

    if type(x) in num_types:
        return True

    return False

mix = [3.14, 'pi', 2.71, 'e', 9.8, 'g']

nums = list(filter(is_number, mix))

print(nums)
