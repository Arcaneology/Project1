import pymysql.cursors
import pandas as pd

#方法1
'''
db = pymysql.connect('localhost','root','937835','demo')
cursor = db.cursor()
sql = 'select * from hy_orderitem_20170410'   #返回表行数
print(cursor.execute(sql))
'''

#方法2
connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='937835',
    db='demo',
    charset='utf8mb4',  # 默认值
    cursorclass=pymysql.cursors.DictCursor)

cur = connection.cursor()  # 建立游标
cur.execute('select * from hy_order_20170410')
result_1 = cur.fetchone()  # 获取一条记录
print(result_1)
result_all = pd.DataFrame(cur.fetchall())  # 获取所有记录并用pandas整理为表格形式
print(result_all)

# cur.execute('create table demo(a int)')
# cur.execute('insert into demo values(3)')
# connection.commit()
cur.execute('select * from demo')
r_demo = cur.fetchall()
r_demo = pd.DataFrame(r_demo)

print(r_demo)
