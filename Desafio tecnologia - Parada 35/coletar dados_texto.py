import os, requests
from bs4 import BeautifulSoup

url = requests.get('https://www.vista-se.com.br/')
html = url.content

site = BeautifulSoup(html, 'html.parser')
html_identado = site.prettify()

arquivo =open("site.txt", "w")
arquivo.write(html_identado)

arquivo.close()

os.system("pause")