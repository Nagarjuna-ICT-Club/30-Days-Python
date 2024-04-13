f = open('file', 'r')

lines = f.readlines()
for line in lines:
    print(line)

f.close()
