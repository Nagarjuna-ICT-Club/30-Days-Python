import csv

name = ('John', 'Alice', 'Bob')
age = (18, 56, 36)
gender = ('M', 'F', 'M')
country = ('NP', 'CN', 'AU')


with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')

    writer.writerow(['firstname','age','gender','country'])
    for row in zip(name, age, gender, country):
        writer.writerow(row)
