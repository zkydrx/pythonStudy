# -*- coding: UTF-8 -*-
# 操作文件和目录
# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
#
# 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
#
# 打开Python交互式命令行，我们来看看如何使用os模块的基本功能：
import os
os.name # 操作系统类型
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
print(os.environ.get('x','default')) # =>default
