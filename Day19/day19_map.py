def first_last_letter(s):
    first = s[0]
    last = s[-1]

    return first + last

colors = ['red', 'blue', 'green']


first_last = list(map(first_last_letter, colors))

print(first_last)
