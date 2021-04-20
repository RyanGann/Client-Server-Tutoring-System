# This file demonstrates how https requests can be made using python.
# Use this documentation as a guide: 
# https://realpython.com/python-requests/#getting-started-with-requests

import requests
import sys

'''
response = requests.get('http://quanthu.life:8000/users')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

#Can do .json() instead of .text to store the data in a dictionary that can be
#acessed by key.

print(response.text)
posts = requests.post('http://quanthu.life:8000/users', data={"_id":"1222", "username": "ryan", "email": "rgann2@una.edu","password":"12345" ,"phone":"2054956944","role":"student","lastActivityDateTime":"04/20/2021","isActive":true})
print(posts.text)
'''
sys('curl -X GET "http://quanthu.life:8000/users" -H  "accept: application/json')
sys('curl -X POST "http://quanthu.life:8000/users" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"_id\": \"12345\",\"username\":\"rgann\",\"email\":\"rgann2@una.edu\",\"password\":\"Ham1234!\",\"phone\":\"2054956944\",\"role\":\"admin\",\"lastActivityDateTime\":\"04/20/2021\",\"isActive\":true}"')
sys('curl -X GET "http://quanthu.life:8000/users" -H  "accept: application/json')