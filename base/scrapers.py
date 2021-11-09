import datetime
import requests
from bs4 import BeautifulSoup
from dateutil import parser
from .models import Article


def get_autosport():
    res = requests.get('https://www.autosport.com/f1/news/')
    soup = BeautifulSoup(res.text, 'html.parser')
    main = soup.find(class_="ms-content_main")
    articles = main.find_all(class_="ms-item--art")
    base_url = 'https://www.autosport.com'
    for item in articles:
        link = base_url + item.a['href']
        title = item.a['title']
        img = item.find('source', type="image/jpeg")['srcset'].split(' ')[0]
        alt = item.img['alt']
        date = item.time['datetime']
        formatted_date = parser.parse(date)
        a = Article.objects.update_or_create(
            link = link,
            title = title,
            image = img,
            alt = alt,
            date = datetime.datetime.strftime(formatted_date, "%Y-%m-%dT%H:%M:%SZ"),
            site = "Autosport",
            defaults={'link': link}
        )
        print('Executed successfully')


def get_wtf1():
    res = requests.get('https://wtf1.com/topics/formula-1/')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('article')
    base_url = 'https://wtf1.com'
    for item in articles:
        link = base_url + item.a['href']
        title = item.find(class_="entry-title").div.text
        imgstr = item.find(class_="feature-image")['style']
        img = imgstr[imgstr.find('(')+1:imgstr.find(')')]
        alt = item.find(class_="entry-title").div.text
        date = item.time['datetime']
        formatted_date = parser.parse(date)
        a = Article.objects.update_or_create(
            link = link,
            title = title,
            image = img,
            alt = alt,
            date = datetime.datetime.strftime(formatted_date, "%Y-%m-%dT%H:%M:%SZ"),
            site = "WTF1",
            defaults={'link': link}
        )
        print('Executed successfully')
