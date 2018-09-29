import re

test1 = '2 评论  29245 人气'
test2 = '31 评论  2921 人气'
test3 = '0 评论  456 人气'

Test01 = re.search('([0-9]+).....([0-9]+)', test1, re.M | re.I)
print(Test01.group(1))
print(Test01.group(2))

line = "Cats are smarter than dogs";

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print(searchObj.group())
    print(searchObj.group(1))
    print(searchObj.group(2))
else:
    print("Nothing found!!")

def test(t):
    for i in t:
        print(i)
    t.append(1)

t=[1]

for i in range(1,3):
    def test(t)