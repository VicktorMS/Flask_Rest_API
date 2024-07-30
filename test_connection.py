import requests

BASE_URL = 'http://127.0.0.1:5000'

response = requests.put(
        f'{BASE_URL}/video/1',
        {'title': 'Test Title'}
    )
print(response.json())