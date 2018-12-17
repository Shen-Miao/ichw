#!/usr/bin/env python3

"""tile.py: Wall.

__author__ = "ZhuQi"
__pkuid__  = "1800011808"
__email__  = "1800011808@pku.edu.cn"
"""

import copy as c
import turtle as t

global ans
global Alist
li=[]
Alist=[]
ans=[]

def wpossible(m,n,a,b,li,t):
    #判断能否横向放下一块砖，若能则返回一个数组(横坐标，纵坐标，0)；0在此处代表横向放置
    lst=(0,0,0)
    Ta=0
    for j in range(a):
        Tb=0
        di = int(t/m)
        if t+j<len(li) and li[t+j]==0 and int((t+j)/m)==di:
            Ta=Ta+1
    if Ta==a:
        for k in range(b):
            for l in range(a):
                if t+l+k*m<len(li) and li[t+l+k*m]==0:
                    Tb=Tb+1
        if Tb==a*b:
            lst=(t%m,int(t/m),0)
            return lst
    return 'WFalse'

def hpossible(m,n,a,b,li,t):
    #判断能否纵向放下一块砖，若能则返回一个数组(横坐标，纵坐标，1)；1在此处代表纵向放置
    lst=(0,0,0)
    Tb=0
    for j in range(b):
        Ta=0
        di = int(t/m)
        if t+j<len(li) and li[t+j]==0 and int((t+j)/m)==di:
            Tb=Tb+1
    if Tb==b:
        for j in range(a):
            for k in range(b):
                if t+k+j*m<len(li) and li[t+k+j*m]==0:
                    Ta=Ta+1
        if Ta==a*b:
            lst=(t%m,int(t/m),1)
            return lst
    return 'HFalse'

def setfull(k,m,a,b,li,c):
    #将某块砖对应的位置置1（放入）
    if c==0:
        for i in range(a):
            for j in range(b):
                li[(k[0]+k[1]*m)+i+j*m]=1
    elif c==1:
        for i in range(b):
            for j in range(a):
                li[(k[0]+k[1]*m)+i+j*m]=1

def setempty(k,m,a,b,li,c):
    #将某块砖对应的位置置0（取出）
    if c==0:
        for i in range(a):
            for j in range(b):
                li[(k[0]+k[1]*m)+i+j*m]=0
    elif c==1:
        for i in range(b):
            for j in range(a):
                li[(k[0]+k[1]*m)+i+j*m]=0

def arrange(m,n,a,b,li,t):
    #主安排程序
    T=0
    global ans
    global Alist
    resultw=wpossible(m,n,a,b,li,t)#判断第t个位置上能否横放一块砖（对应坐标(t%m,t//m))）
    resulth=hpossible(m,n,a,b,li,t)#判断第t个位置上能否纵放一块砖（对应坐标(t%m,t//m))）
    if resultw=='WFalse' and resulth=='HFalse':#都不行：测试是否完全放好
        if t==m*n:#已全部尝试放入，若放满则加入答案列表，若未满则不加入直接返回
            for i in li:
                T=T+i
            if T==len(li):
                Alist.append(c.deepcopy(ans))
                return
            else:
                return
        else:#若该块无法放置但是还有其他块未尝试能否放入，则继续尝试
            arrange(m,n,a,b,li,t+1)
    elif resultw!='WFalse'and resulth=='HFalse':#可以横放则横放，放完后移除
        ans.append(resultw)
        setfull(resultw,m,a,b,li,0)
        arrange(m,n,a,b,li,t+a)
        ans.remove(resultw)
        setempty(resultw,m,a,b,li,0)
    elif resultw=='WFalse' and resulth!='Hfalse':#可以纵放则纵放，放完后移除
        ans.append(resulth)
        setfull(resulth,m,a,b,li,1)
        arrange(m,n,a,b,li,t+b)
        ans.remove(resulth)
        setempty(resulth,m,a,b,li,1)
    else:#横竖都可以则先横放后移除后纵放再移除
        ans.append(resultw)
        setfull(resultw,m,a,b,li,0)
        arrange(m,n,a,b,li,t+a)
        ans.remove(resultw)
        setempty(resultw,m,a,b,li,0)
        ans.append(resulth)
        setfull(resulth,m,a,b,li,1)
        arrange(m,n,a,b,li,t+b)
        ans.remove(resulth)
        setempty(resulth,m,a,b,li,1)

def convert(m,a,b,List):#将上面方便处理的坐标形式转换为要求的输出类型
    brick=[]
    result=[]
    for i in List:
        if i[2]==0:
            brick=[]
            for j in range(b):
                for k in range(a):
                    brick.append(i[0]+i[1]*m+k+j*m)
            result.append(c.deepcopy(tuple(brick)))
        if i[2]==1:
            brick=[]
            for j in range(a):
                for k in range(b):
                    brick.append(i[0]+i[1]*m+k+j*m)
            result.append(c.deepcopy(tuple(brick)))
    return result

def draw(a,b,list):#画图主程序
    t.shape("circle")
    t.hideturtle()
    t.width(3)
    t.speed(0)
    for i in list:
        t.pu()
        t.goto(i[0]*20,i[1]*20)
        t.pd()
        if i[2]==0:
            t.fd(a*20)
            t.lt(90)
            t.fd(b*20)
            t.lt(90)
            t.fd(a*20)
            t.lt(90)
            t.fd(b*20)
            t.lt(90)
        if i[2]==1:
            t.fd(b*20)
            t.lt(90)
            t.fd(a*20)
            t.lt(90)
            t.fd(b*20)
            t.lt(90)
            t.fd(a*20)
            t.lt(90)
    t.pu()
    t.mainloop()

def main():
    m = int(input("Please input the length of the wall:"))
    n = int(input("Please input the width of the wall:"))
    a = int(input("Please input the length of the brick:"))
    b = int(input("Please input the width of the brick:"))
    #输入部分结束
    for i in range(m*n):
        li.append(0)
    #初始化列表结束
    arrange(m,n,a,b,li,0)
    #安排结束
    Fin=[]
    for i in Alist:
        Fin.append(c.deepcopy(tuple(convert(m,a,b,i))))
    #转化为要求形式结束
    num=0
    Final=[]
    Final=list(set(Fin))
    #除重结束
    if len(Final)==0:
        print(False)
    #若无返回值则认为不能铺
    else:
        for i in Final:
            num=num+1
            print(num,' '*(10-len(str(num))),list(i))
        x=t.numinput('Select one type.','Please select which one you would like to print:',default=None,minval=1,maxval=len(Final)+1)
        draw(a,b,Alist[int(x-1)])
    #有返回值则打印所有情况及序号，用户选择之后画图
if __name__=='__main__':
    main()