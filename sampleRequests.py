import requests as requests

url = 'https://cnnindonesia.com'
try:
    request = requests.get(url)
    if (request.status_code == 200):
        print('success', request.status_code)
        print('content', request.text)
    else:
        print('failed', request.status_code)
except Exception as e:
    print('failed')
    print(f'error = {e}')
