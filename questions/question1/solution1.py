# Create a function that returns true only
# if all the elements of the given list are odd


def is_all_odd(my_list):

    for i in my_list:
        # if the number is even, immediately return False
        if i % 2 == 0:
            return False

    # if no numbers are even, return True
    return True


l1 = [2, 3, 9, 1, 3]
l2 = [3 , 1999, 29, 7]


print(is_all_odd(l1))
print(is_all_odd(l2))

