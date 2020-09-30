from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import requests as r
from tqdm import tqdm
from os import system
from tkinter import Tk, filedialog
import csv
from collections import Counter

java_dict = {}


def metrics_getter(site_url, site_list):
    global java_dict
    sites_link = []
    header_list = {}
    writer.writerow({'Site': site_url, '# of JS files': len(site_list)})

    for site in tqdm(site_list):
        if site in java_dict:
            java_dict[site].append(site_url)
        else:
            java_dict[site] = [site_url]

        complete_header = {}
        header_list = {}

        try:
            response = r.get(site, timeout=2).headers
            for key, value in response.items():
                complete_header[key] = value

        except:
            pass

        if site[0:2] == 'ht':
            try:
                response = r.get(site, timeout=2).headers
                for key,value in response.items():
                    if key in ['Expires','Last-Modified', 'Cache-Control']:
                        header_list[key] = value
            except:
                pass

        elif site[0:2]=='//':
            try:
                response = r.get('http:'+site, timeout=2).headers
                for key, value in response.items():
                    if key in ['Expires','Last-Modified', 'Cache-Control']:
                        header_list[key] = value

            except:
                pass
        elif site[0:2] != '//' and site[0] == '/':
            try:
                response = r.get('http://' + site_url + site, timeout=2).headers
                for key,value in response.items():
                    if key in ['Expires','Last-Modified', 'Cache-Control']:
                        header_list[key] = value
            except:
                pass
        writer.writerow({'Site': '', '# of JS files': '',  'JavaScript Files': site,
                         'Full JavaScript Headers': complete_header,
                         'Headers': header_list})


system('cls')
print("Welcome to the JavaScript Web Crawler!!!"
      "\n--> First, select file containing your websites to crawl for their JavaScript files"
      "\n--> The crawler only accepts .txt files. Follow the examplelist.txt provided."
      "\n --> Caution: Some JavaScript file headers are not loaded because of the request timeout of the site")
print('*********************************************************************************************')
Tk().withdraw()
filename = filedialog.askopenfilename(filetypes=[("Text files", ".txt")],
                                      title='Select Files to Crawl')
driver = webdriver.Chrome(ChromeDriverManager().install())

amount_of_js_files = {}
entire_scripts = []

with open(filename, mode='r') as f:
    content = f.read().splitlines()

with open('data.csv', mode='w', newline='') as f:
    fieldnames = ['Site', '# of JS files', 'JavaScript Files',
                  'Full JavaScript Headers', 'Headers']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    number_of_url = 1
    for url in content:
        print(f'[{number_of_url}/{len(content)}] ' + url, end='')
        counter = 0
        if url.__contains__('http://') or url.__contains__('https://'):
            driver.get(url)

        soup = BeautifulSoup(driver.page_source, "lxml")

        javascript_crawl = [i.get('src') for i in soup.find_all('script') if i.get('src')]
        entire_scripts.extend(javascript_crawl)

        print(f': {len(javascript_crawl)} files')
        metrics_getter(url, javascript_crawl)
        number_of_url += 1


with open('file_repetitions.csv', 'w', newline='') as file:
    new_fieldnames = ['Javascript Files', 'Sites', 'Repetitions']
    writer = csv.DictWriter(file, fieldnames=new_fieldnames)
    writer.writeheader()
    for key,value in java_dict.items():
        writer.writerow({'Javascript Files': key, 'Sites': set(list(value)), 'Repetitions': str(len(set(value)))})
