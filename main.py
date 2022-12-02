from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import datetime

def getText(url):
    req = Request(
        url = url, 
        headers={'User-Agent': 'Mozilla/6.0'})

    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, features="html.parser")
    time = datetime.datetime.now()
    textElem = soup.find('div',attrs={"class":"single-content"}) 
    text = ""
    for element in textElem.find_all('p'):
        text += element.text
    return [url,time,text]





