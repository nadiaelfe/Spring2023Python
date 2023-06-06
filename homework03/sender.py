import requests

# response = requests.get('http://127.0.0.1:5000/status')
# print(response.status_code)
# print(response.text)
# print(response.json()['status'])

name = input('Enter a name: ')
while True:
    text = input('Enter a message: ')
    response = requests.post(
        'http://127.0.0.1:5000/send',

        json={
            'name': name,
            'text': text,

        }
    )
# print(response.text)