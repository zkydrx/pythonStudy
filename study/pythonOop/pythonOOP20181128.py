# -*- coding: UTF-8 -*-
# 文档测试
# 如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。比如re模块就带了很多示例代码：
import re
m = re.search('(?<=abc)def','abcdef')
m.group(0)
print(m.group(0)) # =>def
# 可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致。
#
# 这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，那么，可不可以自动执行写在注释中的这些代码呢？
#
# 答案是肯定的。
#
# 当我们编写注释时，如果写上这样的注释：

def abs(n):
    '''
    Function to get absolute value of number
    example:
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n>=0 else (-n)

# 无疑更明确地告诉函数的调用者该函数的期望输入和输出。
#
# 并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
#
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。
#
# 让我们用doctest来测试上次编写的Dict类：


# 运行python mydict2.py：
#
# $ python mydict2.py
# 什么输出也没有。这说明我们编写的doctest运行都是正确的。如果程序有问题，比如把__getattr__()方法注释掉，再运行就会报错：

# File "myDict2.py", line 8, in __main__.Dict
# Failed example:
#     d1.x
# Exception raised:
#     Traceback (most recent call last):
#       File "C:\Program Files\Python37\lib\doctest.py", line 1329, in __run
#         compileflags, 1), test.globs)
#       File "<doctest __main__.Dict[2]>", line 1, in <module>
#         d1.x
#     AttributeError: 'Dict' object has no attribute 'x'
# **********************************************************************
# File "myDict2.py", line 14, in __main__.Dict
# Failed example:
#     d2.c
# Exception raised:
#     Traceback (most recent call last):
#       File "C:\Program Files\Python37\lib\doctest.py", line 1329, in __run
#         compileflags, 1), test.globs)
#       File "<doctest __main__.Dict[6]>", line 1, in <module>
#         d2.c
#     AttributeError: 'Dict' object has no attribute 'c'
# **********************************************************************
# 1 items had failures:
#    2 of   9 in __main__.Dict
# ***Test Failed*** 2 failures.


# 注意到最后3行代码。当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。所以，不必担心doctest会在非测试环境下执行。
# 小结
# doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。

# 练习
# 对函数fact(n)编写doctest并执行：
