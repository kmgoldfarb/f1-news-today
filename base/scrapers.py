import datetime
import requests
from bs4 import BeautifulSoup
from dateutil import parser
from .models import Article, Driver, Constructor, Race


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
            date = datetime.datetime.strftime(formatted_date, "%B %d, %Y | %H:%M"),
            site = "Autosport",
            defaults={'link': link}
        )


def get_planet_f1():
    res = requests.get('https://www.planetf1.com/news/')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find(class_="articleList__list").find_all(class_="articleList__item")
    now = datetime.datetime.now()
    for item in articles:
        link = item.a['href']
        title = item.h3.text
        img = item.img['data-src'][:-11]
        image = img + '1200x630.jpg'
        alt = item.img['alt']
        date = item.time['datetime']
        formatted_date = parser.parse(date)
        a = Article.objects.update_or_create(
            link = link,
            title = title,
            image = image,
            alt = alt,
            date = datetime.datetime.strftime(formatted_date, "%B %d, %Y | %H:%M"),
            site = "PlanetF1",
            defaults={'link': link, 'image': image}
        )


def get_racer():
    res = requests.get('https://racer.com/category/f1/')
    soup = BeautifulSoup(res.text, 'html.parser')
    main = soup.find(class_='column big category-page')
    articles = main.find_all('article', class_="block big")
    for item in articles:
        link = item.a['href']
        title = item.find(class_="content").h3.a.text.strip()
        img = item.img['src']
        alt = item.img['alt']
        date = item.find(class_="time").text
        formatted_date = parser.parse(date)
        a = Article.objects.update_or_create(
            link = link,
            title = title,
            image = img,
            alt = alt,
            date = datetime.datetime.strftime(formatted_date, "%B %d, %Y | %H:%M"),
            site = "Racer",
            defaults={'link': link}
        )


def get_racefans():
    res = requests.get('https://www.racefans.net/')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('article')
    for item in articles:
        link = item.a['href']
        title = item.h2.text
        img = item.img['srcset'].split(",")[2].strip()[:-4]
        alt = item.img['alt']

        # Need to go onto article page to get date and time
        res2 = requests.get(link)
        soup2 = BeautifulSoup(res2.text, 'html.parser')
        date = soup2.find('time')['datetime']
        formatted_date = parser.parse(date)

        a = Article.objects.update_or_create(
            link = link,
            title = title,
            image = img,
            alt = alt,
            date = datetime.datetime.strftime(formatted_date, "%B %d, %Y | %H:%M"),
            site = "RaceFans",
            defaults={'link': link}
        )


def get_racingnews365():
    res = requests.get('https://racingnews365.com/f1-news')
    soup = BeautifulSoup(res.text, 'html.parser')
    main = soup.find(class_="content-grid__main")
    articles = main.find_all(class_="card--default")
    for item in articles:
        link = item['href']
        title = item.find(class_="card__title").text
        img = item.img['src']
        alt = item.find(class_="card__title").text
        date = item.time['datetime']
        formatted_date = parser.parse(date)
        a = Article.objects.update_or_create(
            link = link,
            title = title,
            image = img,
            alt = alt,
            date = datetime.datetime.strftime(formatted_date, "%B %d, %Y | %H:%M"),
            site = "RacingNews365",
            defaults={'link': link}
        )


def get_sky_sports():
    res = requests.get('https://www.skysports.com/f1/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('div', class_='news-list__item')
    for item in articles:
        link = item.a['href'].strip()
        title = item.find(class_="news-list__headline-link").text.strip()
        img = item.img['data-src']
        alt = item.find(class_="news-list__headline-link").text.strip()
        eu_date = item.find('span', class_='label__timestamp').text
        date_obj = datetime.datetime.strptime(eu_date, "%d/%m/%y %I:%M%p")
        a = Article.objects.update_or_create(
            link = link,
            title = title,
            image = img,
            alt = alt,
            date = datetime.datetime.strftime(date_obj, "%B %d, %Y | %H:%M"),
            site = "Sky Sports",
            defaults={'link': link}
        )


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
            date = datetime.datetime.strftime(formatted_date, "%B %d, %Y | %H:%M"),
            site = "WTF1",
            defaults={'link': link}
        )


def get_driver_standings():
    url = 'https://www.formula1.com/en/results.html/2021/drivers.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')    
    driver_standings = soup.find('table', class_="resultsarchive-table")
    for driver in driver_standings.find_all('tbody'):
        rows = driver.find_all('tr')
        for row in rows:
            position = int(row.find('td', class_="dark").text)
            first_name = row.find('span', class_="hide-for-tablet").text
            last_name = row.find('span', class_="hide-for-mobile").text
            name = f"{first_name} {last_name}"
            nationality = row.find('td', class_="dark semi-bold uppercase").text
            team = row.find('a', class_="grey semi-bold uppercase ArchiveLink").text
            points = float(row.find('td', class_="dark bold").text)
            d = Driver.objects.update_or_create(
                name = name,
                nationality = nationality,
                team = team,
                defaults={"position": position, "points": points}
            )


def get_constructor_standings():
    url = 'https://www.formula1.com/en/results.html/2021/team.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')    
    constructor_standings = soup.find('table', class_="resultsarchive-table")
    for team in constructor_standings.find_all('tbody'):
        rows = team.find_all('tr')
        for constructor in rows:
            position = int(constructor.find('td', class_="dark").text)
            team = constructor.find('a', class_="dark bold uppercase ArchiveLink").text
            points = float(constructor.find('td', class_="dark bold").text)
            c = Constructor.objects.update_or_create(
                team = team,
                defaults={"position": position, "points": points}
            )


def get_upcoming_races():
    url = 'https://www.formula1.com/en/racing/2021.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')    
    races = soup.find_all('div', class_='race-card col-12 upcoming')
    for race in races:
        baseURL = 'https://www.formula1.com/'
        start_date = race.find('span', class_="start-date").text
        end_date = race.find('span', class_="end-date").text
        dates = f"{start_date}-{end_date}"
        month = race.find('span', class_="month-wrapper").text
        title = race.find('div', class_="event-title").text
        country = race.find('div', class_="event-place").text
        sources = race.find_all('source')
        flag = sources[0]['data-srcset'].split(",")[0]
        track_img = sources[1]['data-srcset'].split(',')[0]
        country_link = country.strip().replace(' ', '_')
        link = f"en/racing/2021/{country_link}.html"
        formatted_date = parser.parse(start_date)
        r = Race.objects.update_or_create(
            title = title,
            date = f'{month} {dates}',
            country = country,
            flag = flag,
            track_img = track_img,
            link = f"{baseURL}{link}",
            time = datetime.datetime.strftime(formatted_date, "%B %d %Y"),
            defaults={"title": title}
        )
