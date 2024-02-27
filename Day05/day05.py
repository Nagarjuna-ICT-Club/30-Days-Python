# Take inputs from user and typecast it to int
a = int(input("Number 1: "))
b = int(input("Number 2: "))

if a > b:
    # f-strings allow python expressions inside a string
    # by prefixing the string with f or F
    print(f'{a} is greater than {b}')

# Else if
elif a < b:
    print(f'{a} is less than {b}')

# When if and elif both fail, else will run
else:
    print(f'{a} equals {b}')


# If the evaluation of an expression return True, the code inside that block will run
python_is_amazing = True

if python_is_amazing:
    print('Python is amazing')
else:
    print('Python is not amazing')
