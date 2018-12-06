# -*- coding: UTF-8 -*-
# StringIO和BytesIO
# StringIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
#
# StringIO顾名思义就是在内存中读写str。
#
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO
f = StringIO()
print(f.write('Google is a great company')) # =>25
print(f.write(' ')) # =>1
print(f.write('I like it very much!')) # =>20
print(f.getvalue()) # Google is a great company I like it very much!

# getvalue()方法用于获得写入后的str。
#
# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
from io import StringIO
f = StringIO('alienware\nis\nvery\ngood!')
while True:
    s = f.readline()
    if s =='':
        break
    print(s.strip())
    # alienware
    # is
    # very
    # good!

# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

from io import BytesIO
f = BytesIO()
f.write('我爱你'.encode('utf-8'))
print(f.getvalue()) # =>b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'


# 请注意，写入的不是str，而是经过UTF-8编码的bytes。
#
# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
from io import BytesIO
f = BytesIO(b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0')
print(f.read()) # =>b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'

# 小结
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
