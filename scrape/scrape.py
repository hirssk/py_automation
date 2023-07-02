import requests
from bs4 import BeautifulSoup
import time

class Scrape:
    def __init__(self, url):
        self.url = url
    
    def scrape(self, html_tag, css_class):
        html = requests.get(self.url)
        soup = BeautifulSoup(html.content, 'html5lib')

        for find_html in soup.find_all(html_tag, attrs={'class': css_class}):
            print(find_html.text)
            time.sleep(0.5)

if __name__ == "__main__":
    url = 'https://news.yahoo.co.jp/'
    scraper = Scrape(url).scrape('a', 'sc-dtLLSn dpehyt')