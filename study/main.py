# -*- coding: UTF-8 -*-
from __future__ import division

""" Multiline strings can be written
    using three "s, and are often used
    as comments
"""
####################################################
# 1. Primitive Datatypes and Operators
####################################################
3
1 + 1
5 - 3
10 * 2
35 / 7

x = 11 / 4

z = "%s" % (x)

print(x)
print(35 / 7)
(1 + 3) * 3
True
False

not True
not False
1 == 1
print(1 == 2)
print(1 == 1)
print(1 != 1)
print(2 != 1)
print(1 < 10)
print(1 > 10)
print(2 <= 2)
print(2 >= 2)
print("check", " true or not")
print(1 < 2 < 3)
"This is a String"
'This is also a String'

print("Hello " + "world!")

print("This is a string"[0])

print("%s can be %s" % ("Strings", "interpolated"))

print("{0} can be {1}".format("strings", "formatted"))

print("{name} wants to eat {foot}".format(name="Bob", foot="orange"))

None

print("etc" is None)
# 'is' 可以用来比较对象的相等性
# 这个操作符在比较原始数据时没多少用，但是比较对象时必不可少
print(None is None)
# None,0,和空字符串都被算作False
# 其他的均为True
print("None,0,和空字符串都被算作False")
print(0 == False)
print(not None)
print(not "")

####################################################
## 2. 变量和集合
####################################################

# 很方便的输出
print
'I\'m Python. Nice to meet you！'

# 给变量赋值前不需要事先声明
some_var = 5  # 一般建议使用小写字母和下划线组合来做为变量名
print(some_var)
# 访问未赋值的变量会抛出异常
# 可以查看控制流程一节来了解如何异常处理
# some_other_var  # 抛出 NameError

# if语句可以作为表达式来用
print("yahoo!" if 3 > 4 else 2)

# 用列表来保存序列
li = []
# 可以直接序列化列表
other_li = [4, 5, 6]
print(other_li)
# 在列表的末尾添加元素
li.append(1)  # li现在是[1]
print(li)
li.append(2)  # li现在是[1,2]
print(li)
li.append(4)  # li现在是[1,2,4]
print(li)
li.append(3)  # li现在是[1,2,4,3]
print(li)

# 移除列表第末尾的元素
li.pop()  # => 3 li现在是[1,2,4]
print(li)
# 重新加进去
li.append(3)  # li is now [1,2,4,3] again.

print(li)

# 像其他语言访问数组一样访问列表
print(li[0])
# 访问最后一个元素
print(li[-1])

# 越界会抛出异常
# print(li[5])

# 切片语法需要用到列表的额索引访问
# 可以看作数学之中左闭右开区间
print("左开右闭")
li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li1[5:8])  # =>[6,7,8]
# 省略开头的元素
print(li1[1:])  # =>[2, 3, 4, 5, 6, 7, 8, 9]
# 省略末尾的元素
print(li1[:8])  # => [1, 2, 3, 4, 5, 6, 7, 8]
# 删除特定的元素
del li1[2]  #
print(li1)  # =>[1, 2, 4, 5, 6, 7, 8, 9]
# 合并列表
print("li:")
print(li)
print("other_li:")
print(other_li)

print(li + other_li)  # =>[1, 2, 4, 3, 4, 5, 6]- 并不会不改变这两个列表
print("展示拼接")
print("li:")
print(li)
print("other_li:")
print(other_li)
li.extend(other_li)
print(li)

# 用in 来返回元素是否在列表中
print(1 in li)  # =>True
# 返回列表长度
print(len(li1))  # => 9

# 元组类似于列表，但是它是不可改变的
tup = (1, 2, 3)
print(tup)
print(tup[0])  # => 1
# print(tup[0]=3) #类型错误

# 对于大多数的列表操作，也适用于元组
print('tup length:')
print(len(tup))  # =>3
print(tup + (4, 5, 6, 7))  # => (1, 2, 3, 4, 5, 6, 7)
print(tup[:2])  # => (1,2)
print(2 in tup)  # => True

# 你可以将元组解包赋给多个变量
a, b, c = (1, 2, 3)  # a是1，b是2，c是3
print(a)
print(b)
print(c)
# 如果不加括号，将会被自动视为元组
d, e, f = 4, 5, 6
print(d)
print(e)
print(f)

# 现在我们可以看看交换两个数字是多么容易的事
e, d = d, e  # d是5，e是4
print(d)
print(e)

# 字典用来存储映射关系
empty_dict = {}
# 字典初始化
filled_dict = {"one": 1, "two": 2, "three": 3}
print(empty_dict)
print(filled_dict)
# 字典也用中括号访问元素
print(filled_dict["two"])  # =>1
# 把所有的键保存在列表中
print(filled_dict.keys())  # =>['three', 'two', 'one']

# 键的顺序并不是唯一的，得到的不一定是这个顺序

# 把所有的值保存在列表中
print(filled_dict.values())  # =>[3, 2, 1]和键的顺序相同
# 判断一个键是否存在
print("one" in filled_dict)  # => True
print(1 in filled_dict)  # => False
# 查询一个不存在的键会抛出KeyError
# print(filled_dict["four"]) # KeyError

# 用get 方法来避免KeyError
print(filled_dict.get("one"))  # => 1
print(filled_dict.get("four"))  # => None
# get 方法支持在不存在的时候返回一个默认值
print(filled_dict.get("one", 4))  # => 1
print(filled_dict.get("four", 4))  # =>4

# setdefault 是一个更安全的添加字典元素的方法
filled_dict.setdefault("five", 5)
print(filled_dict.get("five"))  # filled_dict["five"] 的值为5
filled_dict.setdefault("five", 6)
print(filled_dict["five"])  # filled_dict["five"] 的值仍然为5

# 集合存贮无顺序的元素
empty_set = set()
# 初始化一个集合
some_set = set([1, 2, 2, 3, 4])
print(some_set)  # =>set([1, 2, 3, 4])
# Python 2.7之后，大括号可用来表示集合
filled_set = {1, 2, 2, 3, 4, 5, 6, 6, 7, 8}
print(filled_set)

# 向集合添加元素
filled_set.add(9)
print(filled_set)  # =>set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# 用& 来计算集合的交
other_set1 = {3, 4, 5, 6}
other_set2 = {1, 2, 3, 5, 6}
print(other_set1 & other_set2)  # => set([3, 5, 6])
print(other_set1 | other_set2)  # => set([1, 2, 3, 4, 5, 6])

# 用 -来计算集合的差
print(other_set1 - other_set2)  # => set([4])

# 用 in来判断元素是否存在于集合中
print(2 in filled_set)  # => True
print(10 in filled_set)  # => False

####################################################
## 3. 控制流程
####################################################
# 新建一个变量
some_var1 = 5
# 这是个if语句，在python中缩进是很重要的
# 下面的代码片段将会输出 "some_var1 is totally biger than 10"
if some_var1 > 10:
    print
    'some_var1 is totally biger than 10'
elif some_var1 < 10:  # 这个 elif 语句是不必须的
    print
    'some_var1 is smaller than 10'
else:  # 这个 else也不是必须的
    print
    "some_var1 is indeed 10."

"""
用for循环遍历列表
输出：
dog is a mammal
cat is a mammal
mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    print
    "%s is a mammal" % animal

"""
`range(number)` 返回从0到给定数字的列表
输出：
0
1
2
3
"""
for i in range(4):
    print
    i

"""
while循环
输出：
0
1
2
3
"""
x = 0
while x < 5:
    print
    x
    x += 1  # x = x + 1的简写

# 用try/except 块来处理异常
# Python 2.6及以上适用
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print
    "Error: 没有找到文件或读取文件失败"
else:
    print
    "内容写入文件成功"
    fh.close()

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!!!!!!!")
finally:
    print
    "Error: 没有找到文件或读取文件失败"


####################################################
## 4. 函数
####################################################

# 用def来新建函数
def add(x, y):
    print
    "x is %s and y is %s" % (x, y)  # =>x is 333 and y is 555
    return x + y  # 通过return来返回值


# 通过关键字赋值来调用函数
print(add(333, 555))  # => 888
print(add(y=8, x=3))


# 我们也可以定义接受多个变量的函数，这些变量是按照顺序排列的
def varargs(*args):
    return args


print(varargs(1, 2, 3))  # => (1,2,3)


# 我们也可以定义接受多个变量的函数，这些变量是按照关键字排列的
def keyword_args(**kwargs):
    return kwargs


# 实际效果：
print(keyword_args(big="foot", loch="ness"))  # =>{'big': 'foot', 'loch': 'ness'}


# 你也可以同时将一个函数定义成两种形式
def all_the_args(*args, **kwargs):
    print
    args
    print
    kwargs


"""
    all_the_args(1,2,a=3,b=4) prints:
    (1,2)
    {"a":3,"b":4}
"""
# 当调用函数的时候，我们也恶意进行相反的操作，把元组和字典展开为参数
print
"把元组和字典展开为参数"
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
print(all_the_args(*args))  # 等价于foo(1,2,3,4)
print("--------------------")
print(all_the_args(**kwargs))  # 等价于foo(a=3,b=4)
print("--------------------")
print(all_the_args(*args, **kwargs))  # 等价于 foo(1,2,3,4,a=3,b=4)


# 函数在python中是一等公民
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_10 = create_adder(10)
print(add_10(3))

# 匿名函数
(lambda x: x > 3)(3)  # True
print((lambda x: x > 2)(3))

# 内置高阶函数
map(add_10, [1, 2, 3])
print(map(add_10, [1, 2, 3]))  # => [11,12,13]

filter(lambda x: x > 5, [3, 4, 5, 6, 7])
print(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # =>[6, 7]

# 可以用列表方法来对告诫函数进行更巧妙的引用
[add_10(i) for i in [1, 2, 3]]
print([add_10(i) for i in [1, 2, 3]])  # => [11,12,13]

[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6,7]
print([x for x in [3, 4, 5, 6, 7] if x > 5])


####################################################
## 5. 类
####################################################

# 我们新建的类是从object类中继承的
class Human(object):
    # 类属性，由所有类的对象共享
    species = "H. sapiens"

    # 基本构造函数
    def __init__(self, name):
        # 将参数付给对象成员属性
        self.name = name

    # 成员方法，参数要有self
    def say(self, msg):
        return "%s:%s" % (self.name, msg)

    # 类方法由所有类的对象共享
    # 这类方法在调用时，会把类本身传给第一个参数
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法是不需要类和对象的引用就可以调用的方法
    @staticmethod
    def grunt():
        return "*grunt*"


# 实例化一个类
i = Human(name="Ian")

print
i.say("hi")

j = Human(name="Joel")
print
j.say("hello")  # 输出 "Joel:hello"

# 访问类的方法
i.get_species()
print(i.get_species())  # =>"H. sapiens"
# 改变共享属性
Human.species = "H. Neanderthalensis"
i.get_species()
print(i.get_species())  # =>H. Neanderthalensis
j.get_species()
print(j.get_species())  # =>H. Neanderthalensis

# 访问静态变量
Human.grunt()
print(Human.grunt())  # => "*grunt*"

####################################################
## 6. 模块
####################################################

# 我们可以导入其他模块
import math

print
math.sqrt(16)  # => 4
# 我们也可以从一个模块中导入特定的函数
from math import ceil, floor

print
ceil(3.7)  # => 4.0
print
floor(3.7)  # => 3.0

# 从模块中导入所有的函数
# 警告：不推荐使用
from math import *

# 简写模块名
import math as m

math.sqrt(16) == m.sqrt(16)
print
math.sqrt(16) == m.sqrt(16)  # => True

# Python 的模块其实只是普通的python文件
# 你也可以创建自己的模块，并且导入它们
# 模块的名字就和文件的名字相同

# 也可以通过下买你的方法查看模块中由什么属性和方法
import math

print
dir(math)
# ['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
