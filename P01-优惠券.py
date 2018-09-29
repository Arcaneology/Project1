'''
P01-

'''

import random
import string

# char_list = [i for i in range(0, 10)]

'''
# 以下为更好的方式获取随机字符串
# 定义一个字符串列表，使得其中包含大小写英文字母和数字
poolOfChars  = string.ascii_letters + string.digits
# 用lambda定义一个函数（包含两个参数x，y ；x代表可选的字符串，y代表总长度，然后循环y次（每次从x里随机选择一个字符）并组合起来）
random_codes = lambda x, y: ''.join([random.choice(x) for i in range(y)])
# 打印随机字符串，x为poolOfChars，y为长度，例子中为15
print(random_codes(poolOfChars, 15))
'''

poolOfChars  = string.ascii_letters + string.digits
random_codes = lambda x, y: ''.join([random.choice(x) for i in range(y)])

n = 15
char_set_n = set()
while True:
    char_set_n.add(random_codes(poolOfChars, n))
    if len(char_set_n) == 16:
        break
print(char_set_n)


