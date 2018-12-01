# -*- coding: UTF-8 -*-
# 调试
# 程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。
#
# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
def foo(s):
    n = int(s)
    print('>>> n =%d'%n)
    return 10/n
def main():
    foo('0')

# main()

# 执行后在输出中查找打印的变量值：
# >>> n =0
# Traceback (most recent call last):
#   File "D:/project/pythonProjects/pythonStudy/study/pythonOop/pythonOOP20181126.py", line 13, in <module>
#     main()
#   File "D:/project/pythonProjects/pythonStudy/study/pythonOop/pythonOOP20181126.py", line 11, in main
#     foo('0')
#   File "D:/project/pythonProjects/pythonStudy/study/pythonOop/pythonOOP20181126.py", line 9, in foo
#     return 10/n
# ZeroDivisionError: division by zero

# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。
# 断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n = int(s)
    assert n !=0, 'n is zero!'
    return 10/n
def main():
    foo('0')
main()

# Traceback (most recent call last):
#   File "D:/project/pythonProjects/pythonStudy/study/pythonOop/pythonOOP20181126.py", line 35, in <module>
#     main()
#   File "D:/project/pythonProjects/pythonStudy/study/pythonOop/pythonOOP20181126.py", line 34, in main
#     foo('0')
#   File "D:/project/pythonProjects/pythonStudy/study/pythonOop/pythonOOP20181126.py", line 31, in foo
#     assert n !=0, 'n is zero!'
# AssertionError: n is zero!
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：

# 关闭后，你可以把所有的assert语句当成pass来看。



# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#
# 如果断言失败，assert语句本身就会抛出AssertionError：
