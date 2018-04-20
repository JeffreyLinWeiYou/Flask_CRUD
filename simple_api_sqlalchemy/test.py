import requests, json
# print(requests.get('http://localhost:5000/todos').json())

# print(requests.post('http://localhost:5000/todos',
#                  headers={'Content-Type': 'application/json'},
#                  data=json.dumps({'task': 'go outside!'})).json())

# print(requests.get('http://localhost:5000/todos/3').json())
# {u'id': 1, u'task': u'go outside!', u'uri': u'http://localhost:5000/todos/1'}
# print(requests.put('http://localhost:5000/todos/1',
#                 headers={'Content-Type': 'application/json'},
#                 data=json.dumps({'task': 'go to the gym2'})).json())
# # {u'id': 1, u'task': u'go to the gym', u'uri': u'http://localhost:5000/todos/1'}
print(requests.delete('http://localhost:5000/todos/1'))
# requests.get('http://localhost:5000/todos').json()