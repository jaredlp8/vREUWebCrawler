from wsgiref import headers
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# headless browser to test javascript code
driver = webdriver.Chrome(ChromeDriverManager().install())
site = 'https://usatoday.com'

driver.get(site)  # add desired link to test
y = requests.get(site)
data = []
results_df = pd.DataFrame()
soup = BeautifulSoup(driver.page_source, "lxml")
javascript_crawl = [i.get('src') for i in soup.find_all('script') if i.get('src')]  # gets javascript

__import__('pprint').pprint(javascript_crawl)
print(javascript_crawl)
print(len(javascript_crawl))

data.append({'Website': site,
             'Header': y.headers,
             'JavaScript files': javascript_crawl,
             '# of JS files': len(javascript_crawl)})

temp_df = pd.DataFrame(data)  # temporary storage
results_df = results_df.append(temp_df).reset_index(drop=True)  # stores all the data

# creates the data csv
results_df.to_csv('headlessdata.csv', sep=',', index=False)

testing = pd.read_csv('headlessdata.csv')
heading = testing.head()
description = testing.describe()
print(heading)

