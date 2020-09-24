import bs4 as bs
import urllib.request
import requests
from requests_html import HTMLSession
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin
import csv
from tqdm import tqdm
import pandas as pd
import time
urls = ['http://lowes.com']
enumerate(urls, start=0)
data = []
driver = webdriver.Chrome(ChromeDriverManager().install())
results_df = pd.DataFrame()
# gets header
for url_link in enumerate(urls) and tqdm(urls):
    driver.get(url_link)
    soup = bs.BeautifulSoup(driver.page_source, 'lxml')
    # get_head = requests.head(url_link)
    # soup_source = soup.prettify()
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
results_df.to_csv('filedata.csv', index=False)
testing = pd.read_csv('filedata.csv')
heading = testing.head(100)
description = testing.describe()
print(heading)


