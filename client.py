import requests

r = requests.post('http://127.0.0.1:5000/login',
                  json={'email': 'you@email.com', 'password': 'yourpass'})

print(r.status_code)
access_token = r.json()['access_token']

r = requests.get('http://127.0.0.1:5000/protected',
                 headers={'Authorization': 'JWT ' + access_token})
print(r.text)
