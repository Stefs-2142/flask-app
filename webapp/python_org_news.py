from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.db import db

from webapp.news.models import News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка.")
        return False


def get_python_news():

    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            print(published)
            try:
                published = datetime.strptime(published, '%b. %d, %Y')
            except ValueError as er:
                published = datetime.now()
                print(er)
            save_news(title, url, published)


def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    print(news_exist)
    if not news_exist:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
