# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:59:04 2017

@author: MuX
"""

import math
def quadratic(a,b,c):
    if b**2-4*a*c<0:
        return '无解'
    else:
        x1=(-b+math.sqrt(b**2-4*a*c))/2*a
        x2=(-b-math.sqrt(b**2-4*a*c))/2*a
        return x1,x2
def power(x,n=2):
    s=1
    for i in range(n):
       s=s*x
    return s   

def add_end1(L=[]):   #这样定义的代码有些问题  就是说当add_end()调用时
    L.append('END')  #会出现多次调用  ['END', 'END', 'END', 'END']
    return L         #因为L第一次调用的时候的地址已经建好了，第二次调用还是那个地址
                     #这种情况的原因也就是L=【】是默认赋值，如果add_end（L=【】）也没问题
def add_end(L=None):
    if L==None:
        L=[]
        L.append('End')
        return L
    else:
        L.append('End')
        return L
def sum_s(*number):   #可变参数
    s=0                   #如果输入数组 在数组前加 *  sum_s(*[list or tuple])
    for i in number:
        s=s+i
    return s
    
def f1(a,b,c=0,*args,**kw):
    print(a,b,c,'args=',args,'kw=',kw)
    #args 是可变参数 kw是关键字参数
def f2(a,b,c=0,*,d,**kw):
    print(a,b,c,'d=',d,'kw=',kw)
    #args 和 kw 都是习惯写法 可以用别的代替
    
    #######################
    #Python中函数的参数很灵活
    #可以直接传入参数
    #也可以通过[]()list 和 tuple 组装之后传入
    #*[]   *()
    #通过关键字参数  **kw
    #可以先组装字典  {}
    #通过**{字典}的方式传参数    
    
####  函数的递归
def fact(n):
    if n==1:
        return 1
    else:
        return fact(n-1)*n
    
def hanoi(n,a,b,c):
    if n==1:
        print(a,'--->',c)
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)
    
    
    
    
    
    
    
    

