import bs4 as bs
import urllib.request
import requests
from requests_html import HTMLSession
from urllib.parse import urljoin
import lxml
import csv
import pandas as pd
url = ['https://google.com', 'https://amazon.com']

# gets header
for index in url:
    session = HTMLSession()
    resp = session.get(index)
    resp.html.render()
    soup = bs.BeautifulSoup(resp.html.html,'lxml')
    x = requests.head(index)
    js_links = [i.get('src') for i in soup.find_all('script') if i.get('src')]
    print("Website:", index)
    print("HTTP header:", x.headers)
    soup_source = soup.prettify()
    print("Crawled HTML: ",soup_source)
    print("JavaScript links: ",js_links)
    # test_df = pd.DataFrame({'Website': index,
    #                         'Header': head_tags
    # })
    # cols = ['Website',
    #         'Header']
    # test_df.to_csv('data/websiteHeaders.csv',
    #                encoding='utf-8', index=False, columns=cols)

# get JavaScript files (work in progress)
# script_files = []
#
# for script in soup.find_all('script') and index in url:
#     if script.attrs.get('src'):
#         script_url = urljoin(index, script.attrs.get("src"))
#         print(script_url)

