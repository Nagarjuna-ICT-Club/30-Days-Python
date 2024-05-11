# Dictionary Comprehension

nums = [2, 3, 4, 5, 6, 7]

# number and its square from `nums`
my_dict = {num: num**2 for num in nums}

print(my_dict)


# Using if condition
my_new_dict = {

    # square of numbers from `nums` that are even
    num: num ** 2 for num in nums if num % 2 == 0
}

print(my_new_dict)
