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
age = 20
if age > 6:
    print('teenager')
elif age >= 18:
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

BMI = weight / (height * height)

if BMI < 18.5:
    print('过轻')
elif BMI in (18.5, 25):
    print('正常')
elif BMI in (25, 28):
    print('过重')
elif BMI in (28, 32):
    print('肥胖')
else:
    print('严重肥胖')

# 循环
# 要计算1+2+3，我们可以直接写表达式：
a = 1 + 2 + 3
# 要计算1+2+3+...+10，勉强也能写出来。
#
# 但是，要计算1+2+3+...+10000，直接写表达式就不可能了。
#
# 为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。
#
# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names = ['Apple', 'Google', 'Microsoft']

for name in names:
    print(name)
# 执行这段代码，会依次打印names的每一个元素：
# Apple
# Google
# Microsoft

# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
#
# 再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：

sum = 0

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)  # =>55

# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，
# 可以生成一个整数序列，再通过list()函数可以转换为list。
# 比如range(5)生成的序列是从0开始小于5的整数：

print(list(range(5)))  # =>[0, 1, 2, 3, 4]

# range(101)就可以生成0-100的整数序列，计算如下：
print(range(101))  # =>range(0, 101)

sum = 0
for x in range(101):
    sum += x;
print(sum)  # =>5050

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现：

sum = 0
n = 9
while n > 0:
    sum += n
    n -= 2
print(sum)  # => 25

# 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print('Hello,', name + '!')

# break
# 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：

n = 1
while n <= 100:
    print(n)
    n += 1
print('END')

# 如果要提前结束循环，可以用break语句：

n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break 语句会结束当前循环
    print(n)
    n += 1
print('END')

# 执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束。
#
# 可见break的作用是提前结束循环。

# continue
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

n = 0
while n < 10:
    n = n + 1
    print(n)
# 上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:# 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
# 执行上面的代码可以看到，打印的不再是1～10，而是1，3，5，7，9。
#
# 可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。

# 小结
# 循环是让计算机做重复任务的有效的方法。
#
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
#
# 要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
#
# 有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
#
# 请试写一个死循环程序。