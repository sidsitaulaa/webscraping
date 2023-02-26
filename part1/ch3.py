from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime 
import random
import time

html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs=BeautifulSoup(html,'html.parser')
# for link in bs.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


random.seed(datetime.datetime.now())
# for link in bs.find('div',{'id':'bodyContent'}).find_all(
#     'a',href=re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

def getLinks(articleUrl):
    html=urlopen(f'http://en.wikipedia.org{articleUrl}')
    bs=BeautifulSoup(html,'html.parser')
    return bs.find('div',{
        'id':'bodyContent'
    }).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))

links=getLinks('/wiki/Kevin_Bacon')

try:
    while(len(links)>0):
        newArticle=links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links=getLinks(newArticle)

except KeyboardInterrupt as k:
    print('Program Ending...')
    time.sleep(3)
    print('Program Ended')

