users = [
    {'name': 'Alice', 'age': 28, 'city': 'New York', 'salary': 70000},
    {'name': 'Bob', 'age': 34, 'city': 'San Francisco', 'salary': 80000},
    {'name': 'Charlie', 'age': 22, 'city': 'New York', 'salary': 50000},
    {'name': 'David', 'age': 30, 'city': 'Los Angeles', 'salary': 60000},
    {'name': 'Eve', 'age': 29, 'city': 'San Francisco', 'salary': 90000},
]

# Return the names of the users whose
# age < 30 and salary > 50000
def high_salary(users):
    names = []
    for user in users:
        if user['age'] < 30 and user['salary'] > 50000:
            names.append(user['name'])
    
    return names

    # Using List Comprehension
    # names = [user['name'] for user in users if user['age'] < 30 and user['salary'] > 50000]
    # return names



print(high_salary(users))

