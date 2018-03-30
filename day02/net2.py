
import sys
import io
import os
print(sys.version)  # 系统版本
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 支持中文

import requests
#from urllib import request

# r = requests.get('https://api.github.com/events')
# print('r:', r.text)
from bs4 import BeautifulSoup
if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='showtxt')
    texts = str(texts)
    print(texts)
    #texts = texts(str_value)
    w = open('/Users/kongjian/Desktop/py/day02/test.txt', 'w')
    w.write(texts)
    w.close()
