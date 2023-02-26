from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


# html=urlopen('http://www.pythonscraping.com/pages/page1.html')
# bs=BeautifulSoup(html.read(),'html.parser')
# print(bs.h1)
# print(bs.body.h1)


# try:
#     html=urlopen('http://www.pythonscraping.com/pages/page1.html')
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print('The server could not be found')
# else:
#     print('It worked!')

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs=BeautifulSoup(html.read(),'html.parser')
        title=bs.body.h1
    except AttributeError as e:
        return None
    return title


title=getTitle('http://www.pythonscraping.com/pages/page1.html')
if title==None:
    print('Title could not be found')
else:
    print(title)
