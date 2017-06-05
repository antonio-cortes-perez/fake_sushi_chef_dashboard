import datetime
import requests

now = datetime.datetime.now()
data = {'channel_id': '12345', 'event': 'start', 'timestamp': now}
response = requests.post('http://127.0.0.1:8000/api/run_event/', data=data, auth=('demo', 'demodemo'))
print(response.status_code)
print(response.json())
