f = open('file', 'w')
f.write('This is the first line.')
f.close()


with open('file', 'w+') as file:
    rows = file.readlines()

for row in rows:
    print(row)
