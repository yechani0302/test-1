from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

html = urlopen("http://jeju-s.jje.hs.kr/jeju-s")
soup = BeautifulSoup(html, "html.parser")
today= str(datetime.date.today())
#today=2023 8 28
# https://jeju-s.jje.hs.kr/jeju-s/food/2023/08/28/lunch
t=today.split("-")
# t=['2023','08','28']

meal_name=["breakfast","lunch","dinner"]
for perieod_name in meal_name:
   url=f"https://jeju-s.jje.hs.kr/jeju-s/food/{t[0]}/{t[1]}/{t[2]}/{perieod_name}"
   print(url)
   html=urlopen(url)
   soup = BeautifulSoup(html, "html.parser")
   bap=soup.select(f'.ulType_food li:nth-child(2) dl dd')

   for a in bap:
      x= a.text.strip().replace(" ","\n")
      print(x)


exit()
url=f'https://jeju-s.jje.hs.kr/jeju-s/food/2023/08/29/breakfast'
print(url)
html=urlopen(url)
soup=BeautifulSoup(html,"html.parser")
bap=soup.select(f'.ulType_food li dd')
print(bap)

