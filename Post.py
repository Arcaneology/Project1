
import requests

url = 'http://www.dy2018.com'
url0 = 'http://www.baidu.com'
d = {'keyboard':'复仇者联盟'}
r = requests.post(url,data=d)
r.encoding = 'utf-8'
print(r.text)

with open('1.html','wb') as f:
    f.write(r.content)