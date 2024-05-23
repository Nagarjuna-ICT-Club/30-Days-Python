normal = ['a', 'b', 'c', 'd']
crypt = ['abcd', 'bcd', 'cd', 'd']

# zip is used to loop over
# multiple sequences at the same time
for n, c in zip(normal, crypt):
    print(f'{n}: {c}')
