# -*- coding: UTF-8 -*-
# 操作文件和目录
# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
#
# 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
#
# 打开Python交互式命令行，我们来看看如何使用os模块的基本功能：
import os

os.name  # 操作系统类型
print(os.name)
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#
# 要获取详细的系统信息，可以调用uname()函数：
# print(os.uname())
# Traceback (most recent call last):
#   File "D:/project/pythonProjects/pythonStudy/study/pythonOop/pythonOOP20181201.py", line 14, in <module>
#     print(os.uname())
# AttributeError: module 'os' has no attribute 'uname'
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\19644\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'ZKY', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'EMACS_HOME': 'D:\\tools\\emacs\\emacs-26.1-x86_64', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\19644', 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk1.8.0_121', 'LOCALAPPDATA': 'C:\\Users\\19644\\AppData\\Local', 'LOGONSERVER': '\\\\ZKY', 'MOZ_PLUGIN_PATH': 'C:\\Program Files (x86)\\Foxit Software\\Foxit PhantomPDF\\plugins\\', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\19644\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files\\Python37\\Scripts\\;C:\\Program Files\\Python37\\;C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Program Files\\Java\\jdk1.8.0_121\\bin;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\TortoiseSVN\\bin;C:\\Program Files\\Git\\cmd;D:\\tools\\cmder_mini\\cmder_mini;C:\\PostgreSQL\\pg10\\bin;C:\\WINDOWS\\System32\\OpenSSH\\;D:\\tools\\emacs\\emacs-26.1-x86_64\\bin;C:\\Users\\19644\\AppData\\Local\\Julia-1.0.0\\bin;D:\\tools\\apache-maven-3.5.4-bin\\apache-maven-3.5.4\\bin;D:\\tools\\sonar\\sonar-scanner-cli-3.2.0.1227-windows\\sonar-scanner-3.2.0.1227-windows\\bin;C:\\Users\\19644\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\19644\\AppData\\Local\\Markdown Monster;C:\\Users\\19644\\AppData\\Local\\Markdown Monster\\Markdown Monster;C:\\Users\\19644\\AppData\\Local\\Microsoft\\WindowsApps', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '2a07', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_HOSTED': '1', 'PYCHARM_MATPLOTLIB_PORT': '59002', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'C:\\Program Files\\JetBrains\\PyCharm 2018.1.5\\helpers\\pycharm_matplotlib_backend;D:\\project\\pythonProjects\\pythonStudy', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\19644\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\19644\\AppData\\Local\\Temp', 'USERDOMAIN': 'ZKY', 'USERDOMAIN_ROAMINGPROFILE': 'ZKY', 'USERNAME': '19644', 'USERPROFILE': 'C:\\Users\\19644', 'WINDIR': 'C:\\WINDOWS'})
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('path'))
# C:\Program Files\Python37\Scripts\;C:\Program Files\Python37\;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Program Files\Java\jdk1.8.0_121\bin;C:\ProgramData\Oracle\Java\javapath;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\Program Files\TortoiseSVN\bin;C:\Program Files\Git\cmd;D:\tools\cmder_mini\cmder_mini;C:\PostgreSQL\pg10\bin;C:\WINDOWS\System32\OpenSSH\;D:\tools\emacs\emacs-26.1-x86_64\bin;C:\Users\19644\AppData\Local\Julia-1.0.0\bin;D:\tools\apache-maven-3.5.4-bin\apache-maven-3.5.4\bin;D:\tools\sonar\sonar-scanner-cli-3.2.0.1227-windows\sonar-scanner-3.2.0.1227-windows\bin;C:\Users\19644\AppData\Local\Microsoft\WindowsApps;C:\Users\19644\AppData\Local\Markdown Monster;C:\Users\19644\AppData\Local\Markdown Monster\Markdown Monster;C:\Users\19644\AppData\Local\Microsoft\WindowsApps
print(os.environ.get('x', 'default'))  # =>default

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
# 查看当前目录的绝对路径
print(os.path.abspath('.'))  # =>D:\project\pythonProjects\pythonStudy\study\pythonOop
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('D:\project\pythonProjects\pythonStudy\study\pythonOop', 'testDir'))
# D:\project\pythonProjects\pythonStudy\study\pythonOop\testDir
# 然后创建一个目录
# os.mkdir('D:\project\pythonProjects\pythonStudy\study\pythonOop\\testDir')
# 删除掉一个目录
# os.rmdir('D:\project\pythonProjects\pythonStudy\study\pythonOop\\testDir')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：
#
# part-1\part-2
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

print(os.path.splitext('D:\project\pythonProjects\pythonStudy\study\pythonOop\\file\\fileA.txt'))
# ('D:\\project\\pythonProjects\\pythonStudy\\study\\pythonOop\\file\\fileA', '.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
#
# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
# 对文件重命名
# print(os.rename('./file/fileA.txt','./file/fileAir.txt'))
# print(os.remove('./file/fileAir.txt'))

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
#
# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：


print([x for x in os.listdir('.') if os.path.isdir(x)])
# ['file', 'interestings', '__pycache__']
# 要列出所有的.py文件，也只需一行代码：
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
# ['hello.py', 'mydict.py', 'myDict2.py', 'mydict_test.py', 'pythonOOP20181113.py', 'pythonOOP20181114.py', 'pythonOOP20181115.py', 'pythonOOP20181116.py', 'pythonOOP20181117.py', 'pythonOOP20181118.py', 'pythonOOP20181119.py', 'pythonOOP20181120.py', 'pythonOOP20181121.py', 'pythonOOP20181122.py', 'pythonOOP20181123.py', 'pythonOOP20181124.py', 'pythonOOP20181125.py', 'pythonOOP20181126.py', 'pythonOOP20181127.py', 'pythonOOP20181128.py', 'pythonOOP20181129.py', 'pythonOOP20181130.py', 'pythonOOP20181201.py']

# 是不是非常简洁？
#
# 小结
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。


# 练习
# 利用os模块编写一个能实现dir -l输出的程序。
#
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os


def getAllDirOrFile():
    for x in os.listdir('.'):
        if os.path.isdir(x):
            print(os.path.abspath('.') + x)
        if os.path.isfile(x):
            print('.' + x)


getAllDirOrFile()

# D:\project\pythonProjects\pythonStudy\study\pythonOopfile
# .hello.py
# D:\project\pythonProjects\pythonStudy\study\pythonOopinterestings
# .mydict.py
# .myDict2.py
# .mydict_test.py
# .pythonOOP20181113.py
# .pythonOOP20181114.py
# .pythonOOP20181115.py
# .pythonOOP20181116.py
# .pythonOOP20181117.py
# .pythonOOP20181118.py
# .pythonOOP20181119.py
# .pythonOOP20181120.py
# .pythonOOP20181121.py
# .pythonOOP20181122.py
# .pythonOOP20181123.py
# .pythonOOP20181124.py
# .pythonOOP20181125.py
# .pythonOOP20181126.py
# .pythonOOP20181127.py
# .pythonOOP20181128.py
# .pythonOOP20181129.py
# .pythonOOP20181130.py
# .pythonOOP20181201.py
# D:\project\pythonProjects\pythonStudy\study\pythonOop__pycache__


from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))


#       0  2018-12-08 21:46  file/
#        114  2018-11-27 21:42  hello.py
#          0  2018-11-26 01:01  interestings/
#        361  2018-12-02 23:09  mydict.py
#        914  2018-12-03 20:08  myDict2.py
#        815  2018-12-02 23:11  mydict_test.py
#       8639  2018-11-15 00:01  pythonOOP20181113.py
#       6431  2018-11-15 00:26  pythonOOP20181114.py
#       8378  2018-11-16 00:19  pythonOOP20181115.py
#       7388  2018-11-18 01:04  pythonOOP20181116.py
#       2549  2018-11-19 23:15  pythonOOP20181117.py
#       2845  2018-11-19 22:42  pythonOOP20181118.py
#       4006  2018-11-20 23:33  pythonOOP20181119.py
#       8516  2018-11-22 00:20  pythonOOP20181120.py
#      22613  2018-11-26 00:30  pythonOOP20181121.py
#       3145  2018-11-27 08:55  pythonOOP20181122.py
#      10095  2018-11-28 22:07  pythonOOP20181123.py
#       6104  2018-11-29 22:45  pythonOOP20181124.py
#      12632  2018-11-30 23:20  pythonOOP20181125.py
#       6054  2018-12-01 23:36  pythonOOP20181126.py
#       6803  2018-12-03 19:50  pythonOOP20181127.py
#       3142  2018-12-03 20:14  pythonOOP20181128.py
#     167197  2018-12-06 00:24  pythonOOP20181129.py
#       1700  2018-12-06 23:32  pythonOOP20181130.py
#      10485  2018-12-08 22:06  pythonOOP20181201.py
#          0  2018-11-27 21:43  __pycache__/
