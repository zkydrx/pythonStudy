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

print("%s can be %s") % ("Strings", "interpolated")

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
print "I'm Python. Nice to meet you！"

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
