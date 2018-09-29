import numpy as np
import random

'''
lst2 = [[1, 2], [3, 4]]
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)
print(arr2[0, 1])

print('-'*20)
arr = np.random.randn(2, 4)
r_arr = arr.reshape(4, 2)
print(arr)
print(r_arr)
# 此处改变r_arr中的值，也会影响到其reshape前的变量的值
r_arr[0, 0] = 0
print(arr)
print(r_arr)
# 此处copy一个arr，新的arr上的修改不会影响原arr
print('-'*20)
arr_c = arr.copy()
arr_c[1, 1] = 1
print(arr)
print(arr_c)
'''
'''
# 数组基本运算
arr3 = np.arange(25).reshape(5, 5)
print(arr3)
print(arr3.T)           # 对arr3进行转置
print()
print(arr3[2, 1:4])     # arr3第2行第2~4个字符
print()
print(arr3[:, 2])       # arr3第3列
print(arr3[2, :])       # arr3第3行
print(arr3[1])          # arr3第2行

print()
print(arr3.dtype)       # 数据格式
print(arr3.size)        # 元素个数
print(arr3.ndim)        # 维度
print(arr3.shape)       # shape
print(arr3.nbytes)      # 空间大小
print()
# 最小值 , 最大值
print(arr3.min(), arr3.max())
# 求和 , 乘积
print(arr3.sum(), arr3.prod())
# 算数平均数 , 方差
print(arr3.mean(), arr3.std())
# 第一维度求和: 按列求和
print(arr3.sum(axis=0))
# 第二维度求和: 按行求和
print(arr3.sum(axis=1))
print()
# 以3*4*5*6数组的第三个维度求和, 生成新数组,打印其shape
print(np.zeros((3,4,5,6)).sum(axis=2).shape)
'''
'''
# 数组与数组运算
arr1 = np.arange(4)
arr2 = np.arange(10, 14)
print(arr1, arr2)
print(arr1 + arr2)
print(arr1 * arr2)
print(arr1+5)       # 数组的每个元素 +5
print(arr1*5)       # 数组的每个元素 *5

arr3 = np.ones((3, 3))
arr4 = np.arange(3)
print(arr3, arr4)
print(arr3+arr4)    # 行与行相加

print(np.arange(3))
print(np.arange(3).reshape(3, 1))
print(np.arange(3) + np.arange(3).reshape(3, 1))    # 第一个arr中每一行加入第二个arr

x = np.linspace(0, 2*np.pi, 100)    # 将0~2pi间数字平均分为100份,并组成list,名为x
y = np.sin(x)
'''

# 线性代数,不明显区分横向量,列向量
v1 = np.array([2, 3, 4])
v2 = np.array([1, 0, 1])
print(v1, v2, np.dot(v1, v2))   # 点乘
v3 = np.arange(6).reshape(2, 3)
print(v1, v3, np.dot(v3, v1))

