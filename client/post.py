import datetime
import requests

now = datetime.datetime.now()
data = {'token': 'x'}
response = requests.post('http://127.0.0.1:8000/api/channelruns/', data=data, auth=('demo', 'demodemo'))
print(response.status_code)
print(response.json())
run_id = response.json()['id']

data = {'run_id': run_id, 'event': 'start', 'progress': 33, 'timestamp': now}
response = requests.post('http://127.0.0.1:8000/api/events/', data=data, auth=('demo', 'demodemo'))
print(response.status_code)
print(response.json())

data = {'run_id': run_id, 'created': 123.45, 'message': 'mmmm'}
response = requests.post('http://127.0.0.1:8000/api/logs/', data=data, auth=('demo', 'demodemo'))
print(response.status_code)
print(response.json())

data = {'token':'x', 'channel_id': '9876'}
response = requests.put('http://127.0.0.1:8000/api/channelruns/'+str(run_id)+'/', data=data, auth=('demo', 'demodemo'))
print(response.status_code)
print(response.json())
