# -*- coding: UTF-8 -*-
# 获取对象信息
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
#
# 使用type()
# 首先，我们来判断对象类型，使用type()函数：
#
# 基本类型都可以用type()判断：
print(type(123))  # =><class 'int'>
print(type('Str'))  # =><class 'str'>
print(type(None))  # =><class 'NoneType'>
