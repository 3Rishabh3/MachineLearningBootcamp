import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup = bs4.BeautifulSoup(res.text, 'lxml')
for link in soup.find_all('a', href=True):
    print(link['href'])


