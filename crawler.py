import bs4 as bs
import urllib.request
from requests_html import HTMLSession
import lxml

session = HTMLSession()
resp = session.get('https://google.com')
resp.html.render()
soup = bs.BeautifulSoup(resp.html.html,'lxml')
head_tags = soup.find('head')
print(head_tags.prettify())



