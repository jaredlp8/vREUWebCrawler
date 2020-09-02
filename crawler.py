import bs4 as bs
import urllib.request
import requests
from requests_html import HTMLSession
from urllib.parse import urljoin
import csv
import pandas as pd
import time
urls = ['https://google.com.tw', 'https://google.com.hk']
data = []
results_df = pd.DataFrame()
# gets header
for url_link in urls:
    session = HTMLSession()
    session.max_redirects = 60
    resp = session.get(url_link)
    resp.html.render()
    soup = bs.BeautifulSoup(resp.html.html, 'lxml')
    get_head = requests.head(url_link)
    soup_source = soup.prettify()
    js_links = [i.get('src') for i in soup.find_all('script') if i.get('src')]
    site_header = requests.get(url_link)
    # prints for testing purposes
    print("Website:", url_link)
    # print("HTTP header:", get_head.headers)
    # print("Crawled HTML: ", soup_source)
    # print("JavaScript files: ", js_links)
    # print(site_header.headers)
    # print(len(js_links))

    data.append({'Website': url_link,
                 'Header': site_header.headers,
                 'JavaScript files': js_links,
                 '# of JS files': len(js_links)})
    temp_df = pd.DataFrame(data)  # temporary storage
    results_df = results_df.append(temp_df).reset_index(drop=True)  # stores all the data

# creates the data csv
results_df.to_csv('Sites251-275data.csv', index=False)
testing = pd.read_csv('Sites251-275data.csv')
heading = testing.head(100)
description = testing.describe()
print(heading)


