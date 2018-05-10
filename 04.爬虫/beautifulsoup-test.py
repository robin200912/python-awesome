from bs4 import BeautifulSoup
import requests

html = requests.get('http://www.baidu.com').content
node = BeautifulSoup(html, 'lxml')
for node in node.find_all('a'):
    print node.get_text()
    print node.attrs['href']
