# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:28:50 2017

@author: MuX
"""

__auther__='MuX'

##################
#Higher order function
#高阶函数
abs(-10)
#函数的本身也是可以赋值的

def fun(a,b,f):
    return f(a)+f(b)

#高阶函数编程，就是指让函数能够接收别的函数


############### 
#reduce 和 map的用法
###############
#map的输入必须是 一个function 和 一个iterable的数据
#map对interable的每一个元素使用
#输入的function进行计算
#map输出的是一个 iteration
m=map(abs,[-1,-4,9,-5])
list(m)

#reduce 输入与map相同
#作用是将 iterable 的前两个数做处理
#处理后再将结果与后边的数进行处理
 
#reduce 需要从模块中引入
from functools import reduce
def add(a,b):
    return a+b
reduce(add,[1,2,3,4,5])

from functools import reduce 
def fn(x,y):
    return x*10+y
    
def str2int(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

reduce(fn,map(str2int,'23434'))

from functools import reduce
def str2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

reduce(lambda x,y:x*10+y,map(str2num,'1233435'))

L1 = ['adam', 'LISA', 'barT']
def normalize(s):
    return s[0].upper()+s[1:].lower()
list(map(normalize,L1))
def power(a,b):
    c=1
    for i in range(b):
        c=c*a
    return c    
def str2float(s):
    s=s.split('.')
    s1=reduce(lambda x,y:x*10+y,map(str2num,s[0]))
    s2=reduce(lambda x,y:x*10+y,map(str2num,s[1]))
    return s1+s2/power(10,len(s[1]))
################犯了很多错误，

#错误1：list的索引是从0开始的
#错误2：map的结果是一个iteration
#错误3：split 的拼写

def is_palindrome(n):
    n=str(n)
    for i in range(len(n)//2):
        if n[i]==n[len(n)-1]:
            pass
        else:
            return False
    return True    

output = filter(is_palindrome, range(1, 1000))
print(list(output))
'''
filter 函数的输出也是iteration
'''
##############sorted 排序方法

sorted([1,2.4,43,34,2452,54,451])

sorted([1,-2.4,-43,34,-2452,54,451],key=abs)

######可以在sorted函数中加入key=abs这类的控制字
#控制排序的效果
'''
必须使用key=函数名  
'''
sorted(['Alpha','Beta','Gamma','Delta','Epsilon','Zeta'])
sorted(['Alpha','Beta','Gamma','Delta','Epsilon','Zeta'],key=str.lower,reverse=True)
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score,reverse=1)
print(L2)

##############利用Python函数返回函数
def lazy_sum(*args):
    def sum_s():
        x=0
        for n in args:
            x=x+n
        return x
    return sum_s

###
###返回函数之后，相当于原来的函数没有运行结束
#返回的还是一个函数，只有再次调用这个函数
#才能算出来真实的返回值
'''
lazy_sum(2123,34,454,23)
Out[52]: <function __main__.lazy_sum.<locals>.sum_s>

f=lazy_sum(2123,34,454,23)
f()
Out[55]: 2634
'''
def count():
    i=[]
    for j in range(1,4):
        def power1():    #()中不应该加J
            return j*j
        i.append(power1)
    return i
f1,f2,f3=count()

#在必须要用循环的情况下，可以分开写
#但是一般情况下，返回函数时，不要用循环
def count2():
    fx=[]
    def f(i):
        def g():
            return i*i
        return g
    for i in range(1,4):
        fx.append(f(i))
    return fx

###/匿名函数
##lambda 是匿名函数的开头
f=lambda x:x*x

####装饰器
###每个函数都有一个名字属性
count2.__name__
#现在需要增强函数的功能在函数运行前后加入打印日志的功能
#一个一般的装饰器
def log(func):
    def wrapper(*args,**kw):
        print('Call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper   

@log
def nonono():
    print('nonono')

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s()'%(text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#完整的decorator 的写法
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args ,**kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s call %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s front call %s():'%(text,func.__name__))
            func(*args,**kw)
            print('%s end call %s():'%(text,func.__name__))
        return wrapper
    return decorator
    
####装饰器是用在函数的定义阶段
@log2('funny')
def abkids():
    print('荡胸生曾云，决眦入归鸟')
    
    ###偏函数
    #functools中的一个功能
    #通过functools.partial()
    #形成一个新的带偏置的函数
    
int8=functools.partial(int,base=8)
    
    ####输入为一个‘534535345’类型的
    ###数据
    ##模块
    
    
    
    
    
    
