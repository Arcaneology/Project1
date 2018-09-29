import requests
from http.cookiejar import LWPCookieJar
import re
from lxml import etree
import time
from zheye import zheye  # 导入zheye，用于识别图片中倒立文字坐标


class LoginZhihu(object):
    def __init__(self):
        # 初始化发送请求的session和headers
        self.session = requests.session()
        self.session.cookies = LWPCookieJar(filename='cookies.txt')
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Host': 'www.zhihu.com',
            'Referer': 'https://www.zhihu.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }


def _get_xsrf(self):
    # 发送get请求，获取xsrf值
    response = self.session.get('https://www.zhihu.com/', headers=self.headers).content
    html = etree.HTML(response)
    xsrf = html.xpath('//input[@name="_xsrf"]/@value')[0]
    return xsrf


def _get_captcha(self):
    # 下载验证码图片，解析倒立文字坐标
    r = str(int(time.time() * 1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r=%s&type=login&lang=cn" % r
    response = self.session.get(captcha_url, headers=self.headers).content
    with open('captcha_cn.gif', 'wb') as f:
        f.write(response)
    positions = zheye().Recognize('captcha_cn.gif')

    input_points = []
    for pos in positions:
        tmp_str = '[' + str('%.2f' % (pos[1] / 2)) + ','
        tmp_str += str('%.2f' % (pos[0] / 2)) + ']'
        input_points.append(tmp_str)
    return ','.join(input_points)


def login(self, account, password):
    # 使用账号和密码登录，并保存cookie到本地文件
    while True:
        if re.match('1\d{10}', account):
            url = 'https://www.zhihu.com/login/phone_num'
            data = {
                '_xsrf': self._get_xsrf(),
                'phone_num': account,
                'password': password,
                'captcha': '{"img_size": [200, 44], "input_points": [%s]}' % self._get_captcha(),
                'captcha_type': 'cn',
            }
        elif '@' in account:
            url = 'https://www.zhihu.com/login/email'
            data = {
                '_xsrf': self._get_xsrf(),
                'email': account,
                'password': password,
                'captcha': '{"img_size": [200, 44], "input_points": [%s]}' % self._get_captcha(),
                'captcha_type': 'cn',
            }
        else:
            print('账号不符合邮箱或手机格式')
            break
        response = self.session.post(url, data=data, headers=self.headers).json()['msg']
        print(response.text)
        if '登录成功' in response:
            self.session.cookies.save()
            break
        elif '账号或密码错误' in response:
            break
