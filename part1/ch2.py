from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs=BeautifulSoup(html.read(),'html.parser')

# namelist=bs.find_all('span',{'class':'green'})


# for name in namelist:
#     print(name.get_text())


# print(bs.find_all(['h1','h2']))

# print(bs.find_all(text='the prince'))
# print(bs.find_all(class_='green'))


# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

# for child in bs.find('table',{'id':'giftList'}).children:
#     print(child)



# for child in bs.find('table',{'id':'giftList'}).tr.next_siblings:
#     print(child)


# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
# print(bs.find('img',{
#     'src':'../img/gifts/img1.jpg'
# }).parent.previous_sibling.get_text())


# images=bs.find_all('img',{
#     'src':re.compile('\.\./img/gifts/img.*\.jpg')
# })


# for image in images:
#     print(image['src'])















