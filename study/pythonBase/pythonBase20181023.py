# -*- coding: UTF-8 -*-
# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
#
# 比如，列出班里所有同学的名字，就可以用一个list表示：

classesmates = ['Mick', 'Bob', "Tony"]
print(classesmates)  # => ['Mick', 'Bob', 'Tony']

# 变量classmates就是一个list。用len()函数可以获得list元素的个数：
print(len(classesmates))  # =>3

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：

print(classesmates[0])  # =>Mick
print(classesmates[1])  # =>Bob
print(classesmates[2])  # =>Tony
# print(classesmates[3])  # => IndexError: list index out of range
# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
#
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classesmates[-1])  # =>Tony
# 以此类推，可以获取倒数第2个、倒数第3个：
print(classesmates[-2])  # =>Bob
print(classesmates[-3])  # =>Tony
# print(classesmates[-4]) #=>IndexError: list index out of range

# 当然，倒数第4个就越界了。
#
# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classesmates.append("zky")
print(classesmates)  # =>['Mick', 'Bob', 'Tony', 'zky']

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classesmates.insert(1, 'drx')
print(classesmates)  # =>['Mick', 'drx', 'Bob', 'Tony', 'zky']

# 要删除list末尾的元素，用pop()方法：
print("delete before:", classesmates)
classesmates.pop()
print("delete after:", classesmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：

print("delete index 2 before:", classesmates)

classesmates.pop(2)
print("delete index 2 before:", classesmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
print('replace index 0 element before:', classesmates)
classesmates[0] = 'Abbot'
print('replace index 0 element after:', classesmates)

# list里面的元素的数据类型也可以不同，比如:
L = ['apple', 123, True]

# list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))  # =>4

# 要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
p = ['asp', 'php']

s = ['python', 'java', p, 'scheme']

# 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。
#
# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
print(p[1])  # => php
print(s[2][1])  # => php

L = []
print(len(L))  # =>0

# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

classmates = ('Michael', 'Bob', 'Tracy')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
#
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：

t = (1,2,'zky')
print(t)
# 如果要定义一个空的tuple，可以写成()：
t = ()

print(t) #=>()

# 但是，要定义一个只有1个元素的tuple，如果你这么定义：
t = (1)
print(t) #=>1
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t =(1,)
print(t) #=>(1,)

# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
#
# 最后来看一个“可变的”tuple：

t = ('a','b',['A','B'])
print("modify before:",t) #=>('a', 'b', ['A', 'B'])
t[2][0] ='X'
t[2][1] = 'Y'
print('modify after:',t) #=>('a', 'b', ['X', 'Y'])
# 这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
#
# 别急，我们先看看定义的时候tuple包含的3个元素：解说看文档：

