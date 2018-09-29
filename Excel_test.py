import xlsxwriter

'''
# 1. 创建一个Excel文件
workbook = xlsxwriter.Workbook('demo1.xlsx')

# 2. 创建一个工作表sheet对象
worksheet = workbook.add_worksheet()

# 3. 设定第一列（A）宽度为20像素
worksheet.set_column('A:A', 20)

# 4. 定义一个加粗的格式对象
bold = workbook.add_format({'bold': True})

# 5. 向单元格写入数据
# 5.1 向A1单元格写入'Hello'
worksheet.write('A1', 'Hello')
# 5.2 向A2单元格写入'World'并使用bold加粗格式
worksheet.write('A2', 'World', bold)
# 5.3 向B2单元格写入中文并使用加粗格式
worksheet.write('B2', u'中文字符', bold)

# 5.4 用行列表示法（行列索引都从0开始）向第2行、第0列（即A3单元格）和第3行、第0列（即A4单元格）写入数字
worksheet.write(2, 0, 10)
worksheet.write(3, 0, 20)

# 5.5 求A3、A4单元格的和并写入A5单元格，由此可见可以直接使用公式
worksheet.write(4, 0, '=SUM(A3:A4)')

# 5.6 在B5单元格插入图片
worksheet.insert_image('B5', './demo.png')

# 5.7 关闭并保存文件
workbook.close()

mydict = [{'A': '1', 'B': '2'}, {'A': '2', 'B': '4'}, {'A': '3', 'B': '6'}]
workbook = xlsxwriter.Workbook('demo6.xlsx')
worksheet = workbook.add_worksheet('MySheet')
i = 0
for dict in mydict:
    worksheet.write(i, 0, dict['A'])
    worksheet.write(i, 1, dict['B'])
    i = i + 1
'''

import csv

row = ['5', 'hanmeimei', '23', '81']
out = open("test.csv", "a", newline="")
csv_writer = csv.writer(out, dialect="excel")
csv_writer.writerow(row)
