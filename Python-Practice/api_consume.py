import requests
import json

response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')
print(response)
print(response.status_code)
print(response.json()['items'])

for questions in response.json()['items']:
    print(questions['title'])
    print(questions['link'])
    print()

for data in response.json()['items']:
    if (data['owner']['user_type']) == 'registered':
        print(data['owner']['display_name'])
        print()



    

