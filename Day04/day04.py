# A dictionary that maps chocolate and its rating
ratings = {
    "guylian": 3.5,
    "toffee": 3,
    "rabbit": 4,
    "milky": 4
}

# Read a value from dictionary
r = ratings.get("rabbit")
print(r)

# Get a list of keys from a dictionary
k = ratings.keys()
print(k)

# Get a list of values from a dictionary
v = ratings.values()
print(v)

# Add a new key-value pair
ratings["newchocolate"] = 5
print(ratings)

# Remove an item from the dictionary
ratings.pop("toffee")
print(ratings)
