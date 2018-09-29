import requests
import random
import re
import time
import csv
from bs4 import BeautifulSoup
import pymysql.cursors
import xlsxwriter


def get_html(url):

    headersChrome = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                                   '63.0.3239.132 Safari/537.36'}
    headersIE = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2;'
                               '.NET CLR 2.0.50727;.NET CLR 3.5.30729; .NET CLR 3.0.30729; '
                               'Media Center PC 6.0; .NET4.0C; .NET4.0E'}
    headersSafari = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                                   'AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'}
    try:
        r = requests.get(url, headers=headersSafari, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('ERROR: get_html:' + url)
        return 'ERROR: get_html:' + url


def get_catalog(url):
    cats = []

    soup = BeautifulSoup(get_html(url), 'lxml')
    catalogtext = soup.find_all('div', class_='recommend')[1]
    catalogs = catalogtext.find('div', class_='directoryArea').find_all('p')
    for c in catalogs:
        try:
            cat = {}
            cat['name'] = c.find('a').get_text()
            cat['link'] = 'http://m.booktxt.net' + c.find('a')['href']
            cats.append(cat)
        except:
            cat = {}
            cat['name'] = 'ERROR'
            cat['link'] = 'NULL'
            cats.append(cat)
            print('ERROR')
    return cats


def csv_catalog(url):
    print('Link:' + url)

    with open('PY/圣墟目录te.csv', 'a', newline='') as my_csv:
        csv_writer = csv.writer(my_csv, dialect='excel')
        for c in get_catalog(url):
            csv_writer.writerow([c['name'], c['link']])
        print('Done!')

    '''
    try:
        out = open('圣墟目录t.csv', 'a', newline='')
        csv_writer = csv.writer(out, dialect="excel")
        for c in get_catalog(url):
            csv_writer.writerow([c['name'], c['link']])
    finally:
        print('Done!')
    '''

def out_database(url):
    print('Link:' + url)


if __name__ == '__main__':
    urllist = ['http://m.booktxt.net/wapbook/2219-{}.html'.format(str(i)) for i in range(1, 3)]
    urllist[0] = 'http://m.booktxt.net/wapbook/2219.html'
    for urls in urllist:
        csv_catalog(urls)

# url = 'http://m.booktxt.net/wapbook/2219.html'
# csv_catalog(url)



#以下为读取文章内代码
'''
def get_content(url):

    soup = BeautifulSoup(get_html(url), 'lxml')

    text = soup.find('div', class_='Readarea ReadAjax_content').get_text().replace('    ', '\n',)

    title = soup.find('span', class_='title').get_text()
    nextlink = 'http://m.booktxt.net' + soup.find('a', class_='Readpage_down')['href']

    return title + text + nextlink

def out_text(url):
    with open('my_text.txt','w') as myFile:
        myFile.write(str(get_content(url)))
        myFile.close()

url = 'http://m.booktxt.net/wapbook/2219_1485868.html'
out_text(url)
'''
