import datetime
import requests
import pprint
import unicodedata
from bs4 import BeautifulSoup
from dateutil import parser
from .models import Article, Driver, Constructor



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
            date = datetime.datetime.strftime(formatted_date, "%B %d, %Y %H:%M"),
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
            date = datetime.datetime.strftime(formatted_date, "%B %d %Y, %H:%M"),
            site = "WTF1",
            defaults={'link': link}
        )
        print('Executed successfully')

def get_driver_standings():
    url = 'https://www.formula1.com/en/results.html/2021/drivers.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')    
    driver_standings = soup.find('table', class_="resultsarchive-table")
    for driver in driver_standings.find_all('tbody'):
        rows = driver.find_all('tr')
        for row in rows:
            position = int(row.find('td', class_="dark").text)
            
            last_name = row.find('span', class_="hide-for-mobile").text
            formatted_name = unicodedata.normalize('NFD', last_name)
            
            nationality = row.find('td', class_="dark semi-bold uppercase").text
            team = row.find('a', class_="grey semi-bold uppercase ArchiveLink").text
            points = float(row.find('td', class_="dark bold").text)
            d = Driver.objects.update_or_create(
                position = position,
                last_name = formatted_name,
                nationality = nationality,
                team = team,
                points = points,
                defaults={"position": position, "points": points}
            )
            pprint.pprint(d)


