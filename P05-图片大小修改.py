# **第 0005 题：**
# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

'''
from PIL import Image
import os

path = 'source/0005/pics'
resultPath = 'source/0005/result'
if not os.path.isdir(resultPath):
    os.mkdir(resultPath)
for picName in os.listdir(path):
    picPath = os.path.join(path, picName)
    print(picPath)
    with Image.open(picPath) as im:
        w, h = im.size
        n = w / 1366 if (w / 1366) >= (h / 640) else h / 640
        im.thumbnail((w / n, h / n))
        im.save(resultPath + '/finish_' + picName.split('.')[0] + '.jpg', 'jpeg')
'''

# 以下为另一种解法
from PIL import Image
import glob
import os


def reSize(dirPath, sizeX=100, sizeY=100):
    for file_path in glob.glob(dirPath + '*.jpg'):
        print(file_path)
        with Image.open(file_path) as ori:
            modi = ori.resize((sizeX, sizeY))
            modi.save(os.path.splitext(file_path)[0] + '_modifid' + '.jpg')


if __name__ == '__main__':
    reSize('pics/', 300, 200)
