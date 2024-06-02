import json

# Sample Python dictionary
python_dict = {
  "name": "John Doe",
  "age": 30,
  "married": True,
  "children": ("Alice","Bob"),
  "pets": None,
  "cars": [
    {"model": "Porsche 911 GT3RS", "mpg": 16},
    {"model": "McLaren Artura", "mpg": 39}
  ]
}

# Python Dictionary to JSON
json_parsed = json.dumps(python_dict)

print(json_parsed)
print(type(json_parsed))