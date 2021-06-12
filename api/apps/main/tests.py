import requests

deviceHostname = 'name'
# '''
client = requests.session()
token = client.get('http://127.0.0.1:8000/csrf')

response = requests.post(
    'http://127.0.0.1:8000',
    data={
        # 'csrfmiddlewaretoken': token,
        'deviceHostname': deviceHostname,
        'humidity': 1234.567,
        'pressure': 1234.567,
        'temperature': 1234.567,
    }
)
# '''

# response = client.get('http://127.0.0.1:8000/csrf')

print(response.text)
