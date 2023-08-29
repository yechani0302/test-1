from bs4 import BeautifulSoup
from urllib.request import urlopen
url=f"https://news.daum.net/digital#1"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

for i in range(1,10):
    daum=soup.select(f'body > div.container-doc.cont-category > main > section > div.main-sub > div.box_g.box_news_major > ul > li:nth-child({i}) > strong')
    print(daum)
    daum_url=soup.select(f'body > div.container-doc.cont-category > main > section > div.main-sub > div.box_g.box_news_major > ul > li:nth-child({i}) > strong > a')
    print(daum_url)