# coding = UTF-8


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url="https://map.kakao.com/?from=total&nil_suggest=btn&q=%EA%B0%95%EB%82%A8%EC%97%AD%20%EC%B9%B4%ED%8E%98&tab=place"

result = urlopen(url)
html = result.read()
soup = BeautifulSoup(html, 'html.parser')


for link in soup.find_all('a',{'href':re.compile('https://*')}):
    # print(link.text.strip(), link.get('href'))
    print(link)






