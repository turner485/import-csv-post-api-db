import requests

def send_data_to_api(api_url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, data=data, headers=headers)
    return response