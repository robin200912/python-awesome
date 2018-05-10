from lxml import etree
import requests

a = requests.get('http://www.baidu.com').content
b = etree.HTML(a)
print type(b)

print b.xpath('//a/@href')
for text in b.xpath('//a[1]/text()'):
    print text