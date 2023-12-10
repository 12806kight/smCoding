import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
print(response.json())

responseDelete = requests.delete('https://jsonplaceholder.typicode.com/todos?id=2')

print(responseDelete.json())

responsePost = requests.post('https://jsonplaceholder.typicode.com/todos', data ={"title": 'delectus aut autem',
    "completed": 'false',
    "userId": 1,})

print(responsePost.json())

