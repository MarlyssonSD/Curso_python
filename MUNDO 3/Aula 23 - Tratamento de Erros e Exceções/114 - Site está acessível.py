import requests
import urllib.request

url1 = 'https://www.pudim.com.br/'
url2 = 'https://www.youtube.com/'

try:
    response_youtube = requests.get(url1)
except:
    print(f'Não foi possível se conectark ao site {url1}')
else:
    print(f'Foi possível se conectar ao site {url1}')

try:
    response_pudim = requests.get(url2)
except:
    print(f'Não foi possível se conectar ao site {url2}')
else:
    print(f'Foi possível se conectar ao site {url2}')

