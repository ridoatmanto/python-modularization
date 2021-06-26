import requests as requests
from bs4 import BeautifulSoup

url = 'https://cnnindonesia.com'
try:
    request = requests.get(url)
    if (request.status_code == 200):
        print('success', request.status_code)
        # print('content', request.text)
        soup = BeautifulSoup(request.text, features="html.parser")
        print(f'Request Result for {url}')
        print(f'Title Tag: {soup.title}')
        print(f'Title : {soup.title.string}')
    else:
        print('failed', request.status_code)
except Exception as e:
    print('failed')
    print(f'error = {e}')
