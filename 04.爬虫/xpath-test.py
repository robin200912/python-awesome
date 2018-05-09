from lxml.etree import HTML
import requests

a = requests.get('http://www.baidu.com').content
b = HTML(a)
print b.xpath('//a/@href')