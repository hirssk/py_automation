import requests
from bs4 import BeautifulSoup
import datetime
import time

now_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')

url = 'https://news.yahoo.co.jp/'
html_tag = 'a'
css_class = 'sc-dtLLSn dpehyt'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html5lib')

find_html_list = soup.find_all(html_tag, attrs={'class': css_class})
print(now_time)
for html_list in find_html_list:
    print(html_list.text)
    time.sleep(0.5)