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
        start = int(input("�����뿪ʼ�½�(��1��ʼ):")) - 1
        if start < 0 or start > len(chapter_link) - 1:
            print("��ʼ�½ڴ�������������")
        else:
            break
    return start


def end():
    for txt in range(0, 999):
        end = int(input("����������½�(���Ϊ���½���):")) - 1
        if end < 0 or end > len(chapter_link) - 1:
            print("�����½ڴ�������������")
        else:
            break
    return end


def all():
    filter_chapter_link = r'<a href="(.+?)">.+?</a>'
    book_txt = str(soup.find_all(name="a", attrs={"href": re.compile(r"/\w+/\w+.html")}))
    chapter_link_1 = re.findall(filter_chapter_link, book_txt)  # ����
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
        print("�����ɹ�")
    else:
        print("�ļ��Ѵ���")


def remadir():
    img_path2 = "D:/txt/" + name
    if not os.path.exists(img_path2):
        os.rename(img_path, img_path2)
        print("��ȫ���������!")
    else:
        downloadtime = time.strftime("%Y%m%d%I%M%S", time.localtime())
        os.rename(img_path, img_path2 + downloadtime)
        print("��ȫ��������ɣ�\n" + "�ļ���:" + name + " �Ѵ���,������Ϊ:" + name + downloadtime + "\n" + "�����ظ�����")


def download(url):
    req = urllib.request.Request(url)  # ��������
    req.add_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'}  # �������ͷ
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
               str(book_txt[0]))).strip() + "\n\n"  # �Թ��˺ͱ༭
    f = open("E:/txt/txt/" + order + ".txt", "a")  # a����׷��ģʽ��������
    f.write(book.encode('gbk', 'ignore').decode('gbk'))
    f.close()
    print(name + "�������")


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
        a = quote(input("����������(��ȷ):").encode('GBK'))  # ����һ��ֵ,����ΪGBK,��ת��Ϊurl���� ������ı���ΪGBK��UTF-8��GBK��url���벻һ����
        if len(a) > 1:
            url = "http://www.x23us.us/modules/article/search.php?searchkey=" + a  # ����������
            req = urllib.request.Request(url)  # ��������
            req.add_header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'}  # �������ͷ
            page = urllib.request.urlopen(req).read()  # �����ӣ�����ȡ
            html = page.decode('utf-8')  # �������Ϊgbk������ʾ������ת��Ϊgbk����
            soup = BeautifulSoup(html, "html.parser")
            b = len(soup.find_all(name="div", attrs={"class": "layout"}))
            if b == 0:
                print("�����ɹ�")
                break
            else:
                print("�޽�������������룡")
        else:
            print("����������2���ַ����ȣ�")
    chapter_link = all()[0]
    name = all()[1]
    print("һ����" + str(len(chapter_link)) + "��")
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