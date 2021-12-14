import os, requests
from bs4 import BeautifulSoup

url = requests.get('https://www.vista-se.com.br/')
html = url.content

site = BeautifulSoup(html, 'html.parser')

print(site.prettify())

os.system("pause")