import requests

# GET request
res = requests.get('https://nagarjunaictclub.com/')

# Check status code
print(res.status_code)

# Headers
print(res.headers)

# Response content
print(res.text)
