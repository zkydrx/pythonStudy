# -*- coding: gbk -*-
from urllib.request import quote
import urllib.request
from bs4 import BeautifulSoup
import re
import multiprocessing
import os
import time


def start():
    for txt in range(0, 999):
        start = int(input("请输入开始章节(从1开始):")) - 1
        if start < 0 or start > len(chapter_link) - 1:
            print("开始章节错误，请重新输入")
        else:
            break
    return start


def end():
    for txt in range(0, 999):
        end = int(input("请输入最后章节(最大为总章节数):")) - 1
        if end < 0 or end > len(chapter_link) - 1:
            print("结束章节错误，请重新输入")
        else:
            break
    return end


def all():
    filter_chapter_link = r'<a href="(.+?)">.+?</a>'
    book_txt = str(soup.find_all(name="a", attrs={"href": re.compile(r"/\w+/\w+.html")}))
    chapter_link_1 = re.findall(filter_chapter_link, book_txt)  # 链接
    chapter_link_2 = "http://www.x23us.us" + " http://www.x23us.us".join(chapter_link_1)
    chapter_link = chapter_link_2.split(' ')
    name = soup.h1.string
    return chapter_link, name


def chapter():
    links = []
    i = 0
    for link_chapter in range(start, end + 1):
        links.append(chapter_link[start + i])
        i = i + 1
    return links


def mkdir(path):
    floder = os.path.exists(path)
    if not floder:
        os.makedirs(path)
        print("创建成功")
    else:
        print("文件已存在")


def remadir():
    img_path2 = "D:/txt/" + name
    if not os.path.exists(img_path2):
        os.rename(img_path, img_path2)
        print("已全部下载完成!")
    else:
        downloadtime = time.strftime("%Y%m%d%I%M%S", time.localtime())
        os.rename(img_path, img_path2 + downloadtime)
        print("已全部下载完成！\n" + "文件名:" + name + " 已存在,重命名为:" + name + downloadtime + "\n" + "请勿重复操作")


def download(url):
    req = urllib.request.Request(url)  # 请求链接
    req.add_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'}  # 添加数据头
    page = urllib.request.urlopen(req).read()
    html = page.decode('gbk')
    soup = BeautifulSoup(html, "html.parser")
    book_txt = soup.find_all(name="div", attrs={"id": "content"})
    txt = soup.find_all(name="h1")
    name = re.sub(r'<h1>|</h1>|\|/|<|>|:|\?|\*|"|\|', '', str(txt[0]))
    filter_order = r'http://www.x23us.us/.+?/(.+?).html'
    order = re.findall(filter_order, url)[0]
    book = name + "\n" + (
        re.sub(r'<div id="content" name="content">|</div>|<br/>\n<br/>| |\n', '',
               str(book_txt[0]))).strip() + "\n\n"  # 对过滤和编辑
    f = open("E:/txt/txt/" + order + ".txt", "a")  # a代表追加模式，不覆盖
    f.write(book.encode('gbk', 'ignore').decode('gbk'))
    f.close()
    print(name + "下载完成")


def change():
    txtname = os.listdir("D:/txt/" + name + "/")
    i = 0
    txts = []
    for txt in range(0, len(txtname)):
        a = "D:/txt/" + name + "/" + txtname[i]
        f1 = open(a, "r")
        lines = f1.readlines()
        o = "\n" + "".join(lines)
        txts.append(o)
        f1.close()
        os.remove(a)
        i = i + 1
    txts1 = "".join(txts)
    g = open("D:/txt/" + name + "/" + name + ".txt", "a")
    g.write(txts1)
    g.close()


if __name__ == '__main__':
    for txt in range(0, 999):
        a = quote(input("请输入书名(精确):").encode('GBK'))  # 接受一个值,编码为GBK,再转换为url编码 （顶点的编码为GBK，UTF-8和GBK的url编码不一样）
        if len(a) > 1:
            url = "http://www.x23us.us/modules/article/search.php?searchkey=" + a  # 搜索的链接
            req = urllib.request.Request(url)  # 请求链接
            req.add_header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'}  # 添加数据头
            page = urllib.request.urlopen(req).read()  # 打开链接，并读取
            html = page.decode('utf-8')  # 顶点编码为gbk，把显示的内容转换为gbk编码
            soup = BeautifulSoup(html, "html.parser")
            b = len(soup.find_all(name="div", attrs={"class": "layout"}))
            if b == 0:
                print("搜索成功")
                break
            else:
                print("无结果，请重新输入！")
        else:
            print("请输入至少2个字符长度！")
    chapter_link = all()[0]
    name = all()[1]
    print("一共有" + str(len(chapter_link)) + "章")
    start = start()
    end = end()
    img_path = "D:/txt/txt/"
    mkdir(img_path)
    links = chapter()
    pool = multiprocessing.Pool(processes=10)
    pool.map(download, links)
    pool.close()
    pool.join()
    remadir()
    change()
    time.sleep(5)