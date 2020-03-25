import pip._vendor.requests as requests
import json




userJson = '{"username":"payam","age":"38"}'
#parse to dic

data = json.loads(userJson)
print(data)
print(data['username'])

jsonified = json.dumps(data)
print(jsonified)


response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()
print(data['title'])