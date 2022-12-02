from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
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

source_url, access_datetime, content = getText("https://kun.uz/uz/news/2022/12/02/uchinchi-davlatlarning-kun-tartibimizni-shakllantirishga-tasiri-yoq-sherzod-asadov")

# word = re.findall(r'(?<!\S)[a-zA-Z0-9]\S*[a-zA-Z](?!\S)', content)
# print(word)




