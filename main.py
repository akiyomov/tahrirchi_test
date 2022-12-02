from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import requests
import datetime

url = "https://kun.uz/uz/news/2022/11/30/parda-ortidagi-xususiylashtirish-yirik-aktivlar-qanday-qilib-ofshor-kompaniyalarga-otib-ketmoqda"
def getText(url):
    req = Request(
        url = url, 
        headers={'User-Agent': 'Mozilla/6.0'})

    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, features="html.parser")
    time = datetime.datetime.now()
    textElem = soup.find_all('p',attrs={"dir":"auto"}) 
    text = ""
    for element in textElem:
        text += element.text
    return [url,time,text]





