from bs4 import BeautifulSoup
import requests
import lxml

source = requests.get('http://deadline.com').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

# headline = article.h3.a.text
# print(headline)
print(soup.prettify())

# for article in soup.find_all('article'):
#     headline = article.h3.a.text
#     print(headline)

