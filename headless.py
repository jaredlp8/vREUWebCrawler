from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# headless browser to test javascript code
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://google.com')  # add desired link to test

soup = BeautifulSoup(driver.page_source, "lxml")
javascript_crawl = [i.get('src') for i in soup.find_all('script') if i.get('src')]  # gets javascript

__import__('pprint').pprint(javascript_crawl)
