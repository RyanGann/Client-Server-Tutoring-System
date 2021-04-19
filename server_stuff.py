# This file demonstrates how https requests can be made using python.
# Use this documentation as a guide: 
# https://realpython.com/python-requests/#getting-started-with-requests

# remember to "pip install requests"

import requests

response = requests.get('http://quanthu.life:8000/users')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

#Can do .json() instead of .text to store the data in a dictionary that can be
#acessed by key.
print(response.text)
