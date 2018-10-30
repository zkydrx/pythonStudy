# -*- coding: UTF-8 -*-
# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#
# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print(list(range(1, 11)))  # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)  # =>[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
print([x * x for x in range(1, 11)])  # => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

print([y * y for y in
       range(1, 21)])  # => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([z * z for z in range(1, 21) if z % 2 == 0])  # =>[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABCD#' for n in
       "1234"])  # =>['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4', '#1', '#2', '#3', '#4']

# 三层和三层以上的循环就很少用到了。
#
# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os  # 导入os模块

print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录
# ['pythonAdvancdeFeatures20181030.py', 'pythonAdvancdeFeatures20181031.py', 'pythonBase20181026.py', 'pythonBase20181027.py', 'pythonBase20181029.py']
# ../../ ['.git', '.gitignore', '.idea', 'README.md', 'study']

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}

for k, v in d.items():
    print(k, '=', v)
# x = A
# y = B
# z = C

# 因此，列表生成式也可以使用两个变量来生成list：
print([k + '=' + v for k, v in d.items()])  # => ['x=A', 'y=B', 'z=C']

# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'Apple']
print([s.lower() for s in L])  # =>['hello', 'world', 'apple']

# 小结
# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。

# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

L = ['Hello','Yes','Git',2018,None,'JAVA']

# print([s.lower() for s in L]) #=>AttributeError: 'int' object has no attribute 'lower'

# 使用内建的isinstance函数可以判断一个变量是不是字符串：

print([s.lower() for s in L if isinstance(s,str)]) # =>['hello', 'yes', 'git', 'java']