# -*- coding: UTF-8 -*-
# 进程和线程

# 很多同学都听说过，现代操作系统比如Mac OS X，UNIX，Linux，Windows等，都是支持“多任务”的操作系统。
#
# 什么叫“多任务”呢？简单地说，就是操作系统可以同时运行多个任务。打个比方，你一边在用浏览器上网，一边在听MP3，一边在用Word赶作业，这就是多任务，至少同时有3个任务正在运行。还有很多任务悄悄地在后台同时运行着，只是桌面上没有显示而已。
#
# 现在，多核CPU已经非常普及了，但是，即使过去的单核CPU，也可以执行多任务。由于CPU执行代码都是顺序执行的，那么，单核CPU是怎么执行多任务的呢？
#
# 答案就是操作系统轮流让各个任务交替执行，任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。表面上看，每个任务都是交替执行的，但是，由于CPU的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样。
#
# 真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。
#
# 对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。
#
# 有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。
#
# 由于每个进程至少要干一件事，所以，一个进程至少有一个线程。当然，像Word这种复杂的进程可以有多个线程，多个线程可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。
#
# 我们前面编写的所有的Python程序，都是执行单任务的进程，也就是只有一个线程。如果我们要同时执行多个任务怎么办？
#
# 有两种解决方案：
#
# 一种是启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。
#
# 还有一种方法是启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。
#
# 当然还有第三种方法，就是启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然这种模型更复杂，实际很少采用。
#
# 总结一下就是，多任务的实现有3种方式：
#
# 多进程模式；
# 多线程模式；
# 多进程+多线程模式。
# 同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，有时，任务1必须暂停等待任务2完成后才能继续执行，有时，任务3和任务4又不能同时执行，所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单线程的程序。
#
# 因为复杂度高，调试困难，所以，不是迫不得已，我们也不想编写多任务。但是，有很多时候，没有多任务还真不行。想想在电脑上看电影，就必须由一个线程播放视频，另一个线程播放音频，否则，单线程实现的话就只能先把视频播放完再播放音频，或者先把音频播放完再播放视频，这显然是不行的。
#
# Python既支持多进程，又支持多线程，我们会讨论如何编写这两种多任务程序。
#
# 小结
# 线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
#
# 多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。




# 多进程


# 要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
#
# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
#
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
#
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

import os

print('Process (%s) start...' % os.getppid()) # =>Process (5548) start...
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
#
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
#
# multiprocessing
# 如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
#
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
#
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：

# from multiprocessing import Process
# import os
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...'%(name,os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.'% os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# Parent process 11760.
# Child process will start.
# Process (11760) start...
# Run child process test (17292)...
# Child process end.

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Pool
import os,time,random
# def long_time_task(name):
#     print('Run task %s (%s)'%(name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s run %0.2f seconds'%(name,(end-start)))
#
# if __name__ == '__main__':
#     print('Parent process %s' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waitting for all subprocess done...')
#     p.close()
#     p.join()
#     print('All subprocess done.')





# Process (5548) start...
# Parent process 3008
# Waitting for all subprocess done...
# Process (3008) start...
# Run task 0 (11636)
# Process (3008) start...
# Process (3008) start...
# Process (3008) start...
# Run task 1 (9180)
# Run task 2 (18228)
# Run task 3 (5636)
# Task 1 run 0.30 seconds
# Run task 4 (9180)
# Task 0 run 1.01 seconds
# Task 3 run 0.87 seconds
# Task 2 run 2.33 seconds
# Task 4 run 2.70 seconds
# All subprocess done.

# 代码解读：
#
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
#
# p = Pool(5)
# 就可以同时跑5个进程。
#
# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

# 子进程
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
#
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#
# 下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：

import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
