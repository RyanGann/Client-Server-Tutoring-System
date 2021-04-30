# have to update username, email, password, phone, role, and isActive each time

import json
import requests

url = 'http://quanthu.life:8000/users/60878dcc788898f7f053f6b2'

user = requests.get(url)
if user.status_code == 200:
    print('Success!')
elif user.status_code == 404:
    print('Not Found.')

print(user.text)

new_data = {
    'phone': '2227659090'
}

update = requests.put(url, json = new_data)
resp = json.loads(update.text)
print(resp)
