try:
    result = 0/0
except Exception:
    print('Cannot divide by zero')


a = 10
try:
    for i in a:
        print(i)
except Exception as err:
    print(err)
finally:
    a = a + 5
    print(a)
