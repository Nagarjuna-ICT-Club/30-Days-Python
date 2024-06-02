import json

# Sample JSON data
json_data = '''{
    "id": "665c8188a73f884fbf8ef10c",
    "isActive": true,
    "balance": "$3,802.44",
    "age": 39,
    "eyeColor": "brown",
    "name": "John Doe",
    "gender": "male",
    "company": "NICT",
    "email": "johndoe@nict.com"
}'''

# Parse JSON data to python dictionary
parsed_dict = json.loads(json_data)

print(parsed_dict)
print(type(parsed_dict))
