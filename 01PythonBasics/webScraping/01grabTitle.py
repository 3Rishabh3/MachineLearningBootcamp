import lxml
import bs4
import requests

res = requests.get('https://toscrape.com/')

soup = bs4.BeautifulSoup(res.text, 'lxml')
title = soup.select('title')
print(title[0].getText())
