# -*- coding: UTF-8 -*-
# 我们知道圆的面积计算公式为：
#
# S = πr2
#
# 当我们知道半径r的值时，就可以根据公式计算出面积。假设我们需要计算3个不同大小的圆的面积：
r1 = 12.34
r2 = 9.08
r3 = 73.1

s1 = 3.14*r1*r1
s2 = 3.14*r2*r2
s3 = 3.14*r3*r3

# 当代码出现有规律的重复的时候，你就需要当心了，每次写3.14 * x * x不仅很麻烦，而且，如果要把3.14改成3.14159265359的时候，得全部替换。
#
# 有了函数，我们就不再每次写s = 3.14 * x * x，而是写成更有意义的函数调用s = area_of_circle(x)，而函数area_of_circle本身只需要写一次，就可以多次调用。
#
# 基本上所有的高级语言都支持函数，Python也不例外。Python不但能非常灵活地定义函数，而且本身内置了很多有用的函数，可以直接调用。

# 抽象
# 抽象是数学中非常常见的概念。举个例子：
#
# 计算数列的和，比如：1 + 2 + 3 + ... + 100，写起来十分不方便，于是数学家发明了求和符号∑，可以把1 + 2 + 3 + ... + 100记作：
#
# 100
#
# ∑n
#
# n=1
#
# 这种抽象记法非常强大，因为我们看到 ∑ 就可以理解成求和，而不是还原成低级的加法运算。
#
# 而且，这种抽象记法是可扩展的，比如：
#
# 100
#
# ∑(n2+1)
#
# n=1
#
# 还原成加法运算就变成了：
#
# (1 x 1 + 1) + (2 x 2 + 1) + (3 x 3 + 1) + ... + (100 x 100 + 1)
#
# 可见，借助抽象，我们才能不关心底层的具体计算过程，而直接在更高的层次上思考问题。
#
# 写计算机程序也是一样，函数就是最基本的一种代码抽象的方式。


# Python内置了很多有用的函数，我们可以直接调用。
#
# 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：
#
# http://docs.python.org/3/library/functions.html#abs
#
# 也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
#
# 调用abs函数：

print(abs(100)) # => 100
# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个：
# abs(1,2) # => TypeError: abs() takes exactly one argument (2 given)
# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型：
# abs('a') # =>TypeError: bad operand type for abs(): 'str'

# 而max函数max()可以接收任意多个参数，并返回最大的那个：
print(max(1,2,3,4)) # => 4

# 数据类型转换
# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：

print(int('123')) # => 123
print(float('123.34234')) # => 123.34234
print(str(123123)) # => 123123
print(bool(123)) # => True
print(bool(0)) # => False
print(bool('')) # => False

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

a = abs

print(a(-100)) #=> 100  所以也可以通过a调用abs函数

# 练习
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

print(hex(10)) # => 0xa

print(help()) # help就是帮助函数。
# Welcome to Python 3.7's help utility!
#
# If this is your first time using Python, you should definitely check out
# the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.
#
# Enter the name of any module, keyword, or topic to get help on writing
# Python programs and using Python modules.  To quit this help utility and
# return to the interpreter, just type "quit".
#
# To get a list of available modules, keywords, symbols, or topics, type
# "modules", "keywords", "symbols", or "topics".  Each module also comes
# with a one-line summary of what it does; to list the modules whose name
# or summary contain a given string such as "spam", type "modules spam".
#
# help>

# 小结
# 调用Python的函数，需要根据函数定义，传入正确的参数。如果函数调用出错，一定要学会看错误信息，所以英文很重要！