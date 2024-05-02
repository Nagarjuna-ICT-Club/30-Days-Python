import requests

# POST data
to_post = {
    'username': 'zeroX123',
    'id': 2
}

# POST requests
res = requests.post('https://nagarjunaictclub.com/', data=to_post)

print(res.status_code)

print(res.text)


