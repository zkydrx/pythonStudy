# -*- coding: UTF-8 -*-
# 条件判断
# 计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。
#
# 比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：
age = 20
if age >= 18:
    print('your age is', age)  # => your age is 20
    print('adult')  # => adult
# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
#
# 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)  # => your age is 3
    print('teenager')  # => teenager
# 注意不要少写了冒号:。
# 当然上面的判断是很粗略的，完全可以用elif做更细致的判断：
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')  # =>kid
# lif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
# if < 条件判断1 >:
#     < 执行1 >
# elif < 条件判断2 >:
#     < 执行2 >
# elif < 条件判断3 >:
#     < 执行3 >
# else:
#     < 执行4 >

# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，所以，请测试并解释为什么下面的程序打印的是teenager：
age =20
if age >6:
    print('teenager')
elif age >=18:
    print('adult')
else:
    print('kid')

# if判断条件还可以简写，比如写：
# if x:
#     print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if ['1']:
    print('True')

# 再议 input
# 最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思：
# birth = input('birth:')
# if birth <2000: # TypeError: '<' not supported between instances of 'str' and 'int'
#     print('00前')
# else:
#     print('00后')
#     输入1982，结果报错：
# TypeError: '<' not supported between instances of 'str' and 'int'
# 这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：

temp = input('birth: ')

birth = int(temp)

if birth < 2000:
    print('00前')
else:
    print('00后')

# 再次运行，就可以得到正确地结果。但是，如果输入abc呢？又会得到一个错误信息：
# ValueError: invalid literal for int() with base 10: 'abc'
# 原来int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了。

weight = 80.5
height = 1.75

BMI = weight / (height*height)

if BMI < 18.5:
    print('过轻')
elif BMI in (18.5,25):
    print('正常')
elif BMI in (25,28):
    print('过重')
elif BMI in (28,32):
    print('肥胖')
else:
    print('严重肥胖')
