import bs4 as bs
import urllib.request
from requests_html import HTMLSession
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
    head_tags = soup.find('head')
    print(index)
    print(head_tags.prettify())
    # test_df = pd.DataFrame({'Website': index,
    #                         'Header': head_tags
    # })
    # cols = ['Website',
    #         'Header']
    # test_df.to_csv('data/websiteHeaders.csv',
    #                encoding='utf-8', index=False, columns=cols)
