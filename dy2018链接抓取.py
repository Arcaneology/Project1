'''
抓取dy2018电影全部链接

base_url='http://www.dy2018.com/html/gndy/dyzz/index.html'
后面网页每页index后加上'_n'

目前连续抓取2页会被触发冻结
'''

# 初始化及html读取函数
import requests
import time
import random
from bs4 import BeautifulSoup


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
        r.encoding = 'gb2312'
        return r.text
    except:
        print('ERROR: get_html:' + url)
        return 'ERROR: get_html:' + url


# 获取下载网页的链接
def get_downpage(url):
    pages = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    dyUrl = 'http://www.dy2018.com'

    tableTags = soup.find_all('table', class_='tbspan')
    print('Loading page : ' + url)
    for table in tableTags:
        page = {}
        try:
            page['link'] = dyUrl + table.find('a', class_='ulink')['href']
            pages.append(page)
        except:
            pages.append('ERROR: get_content:' + url)
            print('ERROR: get_content:' + url)
    return pages


# 获取下载网页内每页内部下载链接，返回文件名和下载地址
# ?需要输出为href的内容，但是实际结果为innerHTML的内容
def get_innerContent(url):
    downloadlists = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    # innerTitle = soup.find('dt', class_='title').get_text(strip=True)
    tdTags = soup.find_all('td', attrs={'style': 'WORD-WRAP: break-word'})
    for td in tdTags:
        downloadlist = {}
        try:
            downloadlist['name'] = soup.find('div', class_='title_all').get_text(strip=True)
            downloadlist['score'] = soup.find('div', class_='position').find('strong', class_='rank').get_text(
                strip=True)
            downloadlist['date'] = soup.find('div', class_='position').find('span', class_='updatetime').get_text(
                strip=True)[5:]
            downloadlist['link'] = td.find('a')['href']
            downloadlists.append(downloadlist)
        except:
            downloadlist['name'] = 'ERROR: get_innerContent:'
            downloadlist['score'] = 'ERROR'
            downloadlist['score'] = 'ERROR'
            downloadlist['link'] = url
            downloadlists.append(downloadlist)
            print('ERROR: get_innerContent:' + url)
    return downloadlists


# 此函数连接为每个get_downpage中的子页面url使用get_innercontent进行解析
# get_innerContent会输出一个嵌套字典的列表，此函数将嵌套的字典析出
def load_inner(url):
    linkList = []
    # link是下载页面
    for link in get_downpage(url):
        # key是下载页面中提取的信息组成的字典
        for key in get_innerContent(link['link']):
            try:
                linkList.append(key)
            except:
                linkList.append('ERROR: load_inner:' + url)
    return linkList


# 输出list为文本文件
def out_text(url):
    # myContent = {}
    with open('Dy2018Downlist[{}].txt'.format(str(time.time()).replace(' ', '-')), 'a+') as myFile:
        # with open('Dy2018Downlist.txt', 'a+') as myFile:
        for myContent in load_inner(url):
            try:
                myFile.write('评分:【{}】\t日期：【{}】\t影片名：【{}】\t链接：【{}】\n'.format(myContent['score'], myContent['date'],
                                                                            myContent['name'], myContent['link']))
            except:
                myFile.write('ERROR: out_text:' + url)
    print('File to text Completed!')


# 翻页
def pages(url, deep):
    base_url = url[0:-5]
    url_list = []
    for i in range(0, deep):
        if i > 0:
            url_list.append(base_url + '_' + str(i + 1) + '.html')
        else:
            url_list.append(base_url + '.html')
        print('Loading page {}'.format(str(i + 1)))

    for myurl in url_list:
        out_text(myurl)
        time.sleep(2)
    print('Process Completed!')


if __name__ == '__main__':
    url = 'http://www.dy2018.com/html/gndy/dyzz/index.html'
    deep = 2
    pages(url, deep)

'''
innerurl = 'http://www.dy2018.com/i/98970.html'
# print(get_innerContent(innerurl))
# get_innerContent(innerurl)
# print(load_inner(url))
'''
