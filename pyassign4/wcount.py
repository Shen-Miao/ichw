#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "ZhuQi"
__pkuid__  = "1800011808"
__email__  = "1800011808@pku.edu.cn"
"""

import sys
import urllib.request
import urllib.error

def read(lines):#从'lines'链接读取文本并转换成字符串
    doc = urllib.request.urlopen(lines)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('utf-8')
    return jstr


def convert(jstr):#将符号替换为空格，消除双空格，将字符串分开为列表
    jstr=jstr.lower()
    for i in ['?',',','.','!',';','[',']','*','#',':','/','_','"','&','--','(',')',"'",'\r','\n','\ufeff']:
        jstr = jstr.replace(i, ' ')
    while '  ' in jstr:
        jstr=jstr.replace('  ',' ')
    List = jstr.split(' ')
    return List


def wcount(stringlist, topn=10):#计算单词数量及返回前topn(10)个单词
    Dict = dict()
    List=[]
    for i in stringlist:
        if i != '':
            if i in Dict:
                Dict[i] += 1
            else:
                Dict[i] = 1
    Ndict=sorted(Dict.items(), key=lambda t: t[1], reverse=True)
    if int(topn)>len(Ndict):
        topn=len(Ndict)
    for i in range(int(topn)):
        List.append(Ndict[i])
    return List

def printlist(List):#打印列表
    for i in List:
        print(i[0],' '*(30-(len(i[0])+len(str(i[1])))),i[1])


if __name__ == '__main__':#主程序
    if len(sys.argv)==1:#直接运行时提示运行方法
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    lines = sys.argv[1]
    if len(sys.argv)==3:#如果给了三个参数（文件名，链接，数量为正确输入）
        topn = sys.argv[2]
        try:
            Dict = wcount(convert(read(lines)), topn)
            printlist(Dict)
        except ValueError as e:#输入错误
            if 'invalid literal for int() with base 10' in str(e):
                print('Not a valid number!')
            if 'unknown url type' in str(e):
                print('Not a valid URL!')
        except urllib.error.HTTPError as e:#网页访问错误
            print(e)
            if e.code==404:
                print('Please check your input URL.')
        except urllib.error.URLError as e:#其他URL错误
            print(e)
    elif len(sys.argv)==2:#如果给了两个参数（文件名，链接）
        try:
            Dict = wcount(convert(read(lines)))
            printlist(Dict)
        except ValueError as e:#输入错误
            if 'invalid literal for int() with base 10' in str(e):
                print('Not a valid number!')
            if 'unknown url type' in str(e):
                print('Not a valid URL!')
        except urllib.error.HTTPError as e:#网页访问错误
            print(e)
            if e.code==404:
                print('Please check your input URL.')
        except urllib.error.URLError as e:#其他URL错误
            print(e)
    else:#输入数目错误
        print('Number of parameters exceeded limit!')