import requests
import random
import re
import time
import csv
from bs4 import BeautifulSoup
import xlsxwriter


def get_html(url):
    headersChrome = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                                   '63.0.3239.132 Safari/537.36'}
    headersIE = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2;'
                               '.NET CLR 2.0.50727;.NET CLR 3.5.30729; .NET CLR 3.0.30729; '
                               'Media Center PC 6.0; .NET4.0C; .NET4.0E'}
    headersSafari = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                                   'AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'}
    my_headers = random.choice([headersChrome, headersIE, headersSafari])
    try:
        r = requests.get(url, headers=headersIE, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('ERROR: get_html:' + url)
        return 'ERROR: get_html:' + url


# 获取菜品网页的详情5步  /大概15分钟
def get_food(url):
    foods = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    food_list = soup.find('div', class_='listtyle1_list clearfix')
    food_tag = food_list.find_all('div', class_='listtyle1')
    for div in food_tag:
        food = {}
        try:
            food['name'] = div.find('div', class_='c1').strong.get_text(strip=True)
        except AttributeError:
            food['name'] = 'None'
        try:
            comment = div.find('div', class_='c1').span.get_text(strip=True)
            try:
                food['hot'] = re.search('(^[0-9]+).+', comment, re.I).group(1)
            except AttributeError:
                food['hot'] = 'None'
            try:
                food['discuss'] = re.search('.+ ([0-9]+).人气', comment, re.I).group(1)
            except AttributeError:
                food['discuss'] = 'None'
        except AttributeError:
            food['hot'] = 'None'
            food['discuss'] = 'None'
        try:
            food['author'] = div.find('div', class_='c1').em.get_text(strip=True)
        except AttributeError:
            food['author'] = 'None'
        try:
            food['link'] = div.find('a', class_='big')['href']
        except AttributeError:
            food['link'] = 'None'
        try:
            step_time = div.find('li', class_='li1').get_text()
            try:
                food['step'] = re.search('(^[0-9]+步|.+).+', step_time, re.I).group(1)
            except AttributeError:
                food['step'] = 'None'
            try:
                food['time'] = re.search('.+大概(.+$)', step_time, re.I).group(1)
            except AttributeError:
                food['time'] = 'None'
        except AttributeError:
            food['step'] = 'None'
            food['time'] = 'None'
        try:
            cook_flavor = div.find('li', class_='li2').get_text()
            try:
                food['cook'] = re.search('([\u4E00-\u9FA5]+) / .+', cook_flavor, re.I).group(1)
            except AttributeError:
                food['cook'] = 'None'
            try:
                food['flavor'] = re.search('([\u4E00-\u9FA5]+味)', cook_flavor, re.I).group(1)
            except AttributeError:
                food['flavor'] = 'None'
        except AttributeError:
            food['cook'] = 'None'
            food['flavor'] = 'None'
        foods.append(food)
    return foods


# 获取菜品网页的页数
def food_page(url):
    # foods = []
    outlist = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    # 循环建立子页面查找url列表
    food_urllist = []
    pagenum = soup.find('span', class_='gopage').get_text()
    foodnum = re.findall(r'\d+', pagenum)
    for i in range(0, int(foodnum[0])):
        if i == 0:
            food_urllist.append(url)
        else:
            food_urllist.append(url + '?&page=' + str(i + 1))
    for foodurl in food_urllist:
        print('Loading:' + foodurl)
        outlist.append(get_food(foodurl))
        print('Success!')
    return outlist


def food_style(url):
    stylelist = {}
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    all_stylelist = soup.find('dl', class_='listnav_dl_style1 w990 clearfix')
    stylelists = all_stylelist.find_all('a')
    for style in stylelists:
        stylelist[style.get_text()] = style['href']
    return stylelist


'''
if __name__ == '__main__0':
    url = 'http://www.meishij.net/china-food/caixi/xiangcai/'
    workbook = xlsxwriter.Workbook('demo{}.xlsx'.format(time.time()))
    worksheet = workbook.add_worksheet('FoodSheet')
    t = 0
    for food in food_page(url):
        for dict in food:
            worksheet.write(t, 0, dict['name'])
            worksheet.write(t, 1, dict['hot'])
            worksheet.write(t, 2, dict['discuss'])
            worksheet.write(t, 3, dict['author'])
            worksheet.write(t, 4, dict['link'])
            worksheet.write(t, 5, dict['step'])
            worksheet.write(t, 6, dict['time'])
            worksheet.write(t, 7, dict['cook'])
            worksheet.write(t, 8, dict['flavor'])
            t = t + 1
    workbook.close()
    print('Job Done!')
'''
'''
def write(filename, url):
    worksheet = workbook.add_worksheet('Food-' + filename)
    t = 0
    for food in food_page(url):
        for dict in food:
            worksheet.write(t, 0, dict['name'])
            worksheet.write(t, 1, dict['hot'])
            worksheet.write(t, 2, dict['discuss'])
            worksheet.write(t, 3, dict['author'])
            worksheet.write(t, 4, dict['link'])
            worksheet.write(t, 5, dict['step'])
            worksheet.write(t, 6, dict['time'])
            worksheet.write(t, 7, dict['cook'])
            worksheet.write(t, 8, dict['flavor'])
            t = t + 1
    print('Page Done!')
'''
'''
def write(filename, url):
    t = 0
    for food in food_page(url):
        for dict in food:
            worksheet.write(t, 0, dict['name'])
            worksheet.write(t, 1, dict['hot'])
            worksheet.write(t, 2, dict['discuss'])
            worksheet.write(t, 3, dict['author'])
            worksheet.write(t, 4, dict['link'])
            worksheet.write(t, 5, dict['step'])
            worksheet.write(t, 6, dict['time'])
            worksheet.write(t, 7, dict['cook'])
            worksheet.write(t, 8, dict['flavor'])
            worksheet.write(t, 9, filename)
            t = t + 1
    print('Page Done!')
'''


def writecsv(filename, url):
    for food in food_page(url):
        for dict in food:
            writer.writerow((dict['name'], dict['hot'], dict['discuss'], dict['author'], dict['link'], dict['step'],
                             dict['time'], dict['cook'], dict['flavor'], filename))
    print('Page Done!')


if __name__ == '__main__':
    url = 'http://www.meishij.net/china-food/caixi/chuancai/'
    foodfile = open('MSJ{}.csv'.format(time.time()), 'w+')
    writer = csv.writer(foodfile)
    for key, value in food_style(url).items():
        writecsv(key, value)
    print('Job Done!')

'''
if __name__ == '__main__excel':
    url = 'http://www.meishij.net/china-food/caixi/chuancai/'
    workbook = xlsxwriter.Workbook('MSJ{}.xlsx'.format(time.time()))
    worksheet = workbook.add_worksheet('Food')
    for key, value in food_style(url).items():
        write(key, value)
    workbook.close()
    print('Job Done!')
'''

# 存在问题：write中t不能保留，使得每次引用write函数时都从第一行开始写
