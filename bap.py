from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://jeju-s.jje.hs.kr/jeju-s")
soup = BeautifulSoup(html, "html.parser")

bap = soup.select(".meal_menu ul li")
print("="*50)
print( bap)
print("-"*50)

for m in bap:
   print( m.text.strip() ) 

print("="*50)