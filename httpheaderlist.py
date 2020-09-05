import csv
from tkinter import filedialog, Tk
import requests
# class to obtain HTTP header of a website.
# If added to crawler, it will slow down the crawler and provoke timeouts
Tk().withdraw()
filename = filedialog.askopenfilename(filetypes=[("Text files", ".txt"), ("CSV files", ".csv")],
                                      title='Select Files to Crawl')
with open(filename, mode='r') as f:
    content = f.read().splitlines()

with open('http_header_data.csv', mode='w', newline='') as f:
    fieldnames = ['Site', 'HTTP Header']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for url in content:
        if url.__contains__('http://') or url.__contains__('https://'):
            r = requests.head(url)
        else:
            r = requests.head('http://'+url)

    writer.writerow({'Site': url, 'HTTP Header': r.headers})
