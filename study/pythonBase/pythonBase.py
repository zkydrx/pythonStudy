print("one", "two", "three", "go")

print(100)
print('300 + 3000 =', 300 + 3000)

# Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里
# 任何计算机程序都是为了执行一个特定的任务，有了输入，用户才能告诉计算机程序所需的信息，有了输出，程序运行后才能告诉用户任务的结果。
#
# 输入是Input，输出是Output，因此，我们把输入输出统称为Input/Output，或者简写为IO。
#
# input()和print()是在命令行下面最基本的输入和输出，但是，用户也可以通过其他更高级的图形界面完成输入和输出，比如，在网页上的一个文本框输入自己的名字，点击“确定”后在网页上看到输出信息。
name = input('please enter your name:')

print("hello", name)

a = 100

if a > 0:
    print(a)
else:
    print(-a)

#
# 整数
# Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。
#
# 计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。
#
# 浮点数
# 浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。
#
# 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。
b = 1
c = 3.15
d = 2.34e5
print(b, c, d)

#
# 字符串
# 字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。
#
# 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：
#
# 'I\'m \"OK\"!'
# 表示的字符串内容是：
#
# I'm "OK"!
# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串看看：
print('I\'m ok')

print('\\\n\\')
# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
print(r'\\\n\\zky''*')

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，可以自己试试：
print('''1
2.3
4''')

print('''...''')

# 多行字符串'''...'''还可以在前面加上r使用
print(r'''''1''1''''')
#
# 布尔值
# 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
print(True)
print(False)
#
# 布尔值可以用and、or和not运算。
#
# and运算是与运算，只有所有都为True，and运算结果才是True：

print(True and True)
print(True and False)
print(False and False)
print(False and True)
print(3 > 1 and 6 > 9)

# or运算是或运算，只要其中有一个为True，or运算结果就是True：

print(True or False)

# not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
print(not False)

# 空值
# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
#
# 此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到。
#

# 变量
# 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
#
# 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头，比如：
a = 1

# 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：
temp = 1  # temp 是整数
print(temp)
temp = 'abc'  # temp是字符串
print(temp)

# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，赋值语句如下（// 表示注释）：
temp1: int = 1

# int a = 123; // a是整数类型变量
# a = "ABC"; // 错误：不能把字符串赋给整型变量


# 和静态语言相比，动态语言更灵活，就是这个原因。
#
# 请不要把赋值语句的等号等同于数学的等号。比如下面的代码：

x = 10
x = x + 3

# 如果从数学上理解x = x + 2那无论如何是不成立的，在程序中，赋值语句先计算右侧的表达式x + 2，得到结果12，再赋给变量x。由于x之前的值是10，重新赋值后，x的值变成12。
#
# 最后，理解变量在计算机内存中的表示也非常重要。当我们写：

a = "ABC"

# 时，Python解释器干了两件事情：
#
# 在内存中创建了一个'ABC'的字符串；
#
# 在内存中创建了一个名为a的变量，并把它指向'ABC'。
#
# 也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：

b = a
a = 'XYZ'
print(a)
print(b)

# 最后一行打印出变量b的内容到底是'ABC'呢还是'XYZ'？如果从数学意义上理解，就会错误地得出b和a相同，也应该是'XYZ'，但实际上b的值是'ABC'，让我们一行一行地执行代码，就可以看到到底发生了什么事：
#
# 执行a = 'ABC'，解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：
#
# py-var-code-1
#
# 执行b = a，解释器创建了变量b，并把b指向a指向的字符串'ABC'：
#
# py-var-code-2
#
# 执行a = 'XYZ'，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：
#
# py-var-code-3
#
# 所以，最后打印变量b的结果自然是'ABC'了。


# 常量
# 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：

PI = 3.14
# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
#
# 最后解释一下整数的除法为什么也是精确的。在Python中，有两种除法，一种除法是/：

print(10 / 3)  # =>3.3333333333333335
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
print(9 / 3)  # =>3.0
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
print(10 // 3)  # =>3

# 你没有看错，整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以。
#
# 因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：
print(10 % 3)  # => 1
# 无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。
print(11.3 % 3)

# Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
#
# 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。
#
# 注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。
#
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

# Python的字符串
# 搞清楚了令人头疼的字符编码问题后，我们再来研究Python的字符串。
#
# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：
print("包含中文的str")
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))  # => 65

print(ord('周'))  # => 21608

print(chr(66))  # => B

print(chr(21602))  # =>呢

# 如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587')  # => 中文
# 两种写法完全是等价的。

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：

x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
#
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'))  # =>b'ABC'

print('中文'.encode('utf-8'))  # =>b'\xe4\xb8\xad\xe6\x96\x87'

# print('中文'.encode('ascii')) # =>
# Traceback (most recent call last):
#   File "D:/project/pythonProjects/pythonStudy/study/pythonBase/pythonBase.py", line 214, in <module>
#     print('中文'.encode('ascii')) # =>
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。

# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'))  # =>ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # =>中文

# 如果bytes中包含无法解码的字节，decode()方法会报错：
# print(b'\xe4\xb8\xad\xe6\x96'.decode('utf-8'))
# =>print(b'\xe4\xb8\xad\xe6\x96'.decode('utf-8')) #=>
# UnicodeDecodeError: 'utf-8' codec can't decode bytes in position 3-4: unexpected end of data

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xe6\x96'.decode('utf-8', errors='ignore'))  # =>中

# 要计算str包含多少个字符，可以用len()函数：
print(len('zkydrx'))  # =>6
print(len('中文'))  # =>2

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：

print(b'ABC')  # =>3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # =>6
print(len('中文'.encode('utf-8')))  # =>6
# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
# 在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
#
# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：

# 如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文：


# 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：

print('Hello,%s' % 'World!')

print("Hi,%s you have $%d." %('Abbot',99999))
print("z%s" % 'ky')
#你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

print('%2d-%02d' %(3,1)) #=> 3-01
print('%.2f' % 3.14) #=>3.14

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

print("Age:%s.Gender:%s"%(35,True))
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate:%d%%'%7)

# ormat()
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：

print("Hello,{0},你的银行卡余额是{1:.2f} 比上个星期提升了{2:.2f}%".format("Abbot",359993.324,20.658))

# Python 3的字符串使用Unicode，直接支持多语言。
#
# 当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。Python当然也支持其他编码方式，比如把Unicode编码成GB2312：

print("中国".encode('gb2312')) #=>b'\xd6\xd0\xb9\xfa'

# 但这种方式纯属自找麻烦，如果没有特殊业务要求，请牢记仅使用UTF-8编码。
#
# 格式化字符串的时候，可以用Python的交互式环境测试，方便快捷。