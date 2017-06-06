# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 21:30:59 2017

@author: MuX
"""
#python 高级特性
for i in range(100):
    print('\n',i)
L=list(range(100))

########
'''
切片  与MATLAB十分相似
不同点：
# 开头的那个数字是索引的起始点 
# 后边的数减前边的数 是索引数字的总数
'''
#######

 L[0:15]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

L[1:15]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# 开头的那个数字是索引的起始点 
# 后边的数减前边的数 是索引数字的总数

####对于输出[] {} （）内容的叫做迭代
###在practice-1中已经写过dictionary的迭代了

for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)
''' 
针对两个元素的迭代输出
'''
for x,y in enumerate(['A','B','C']):
    print(x,y)
####enumerate 可以将列表的下标输出出来 


'''
List Comprehensions 列表生成式
'''
[x*x for i in range(1,11)]
[x ** x for x in range(10)]

##################
#两层嵌套的
[x+y for x in 'ABC' for y in 'XYZ']

L = ['Hello', 'World', 18, 'Apple', None]
[S.lower() for S in L if isinstance(S,str)==True]

[S.lower() for S in L if isinstance(S,str)]

#############这个地方太蠢了，可以不加True的
'''
generator   生成器
'''
#########################生成器是用来生成 列表的  生成部分列表供当前的计算
'''
生成器的用法很简单  与 列表生成式类似  把 [] 换成 （）就可以了
'''
g=(x ** x for x in range(10))

def fib(m):
    n,a,b= 0,0,1
    while a<m:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'Done'    
'''
生成器的另一种定义方法
在函数中出现  yield 关键字 函数就会变成生成器
'''
    
    
def fib(m):
    n,a,b= 0,0,1
    while a<m:
        yield b
        a,b=b,a+b
        n=n+1
    return 'Done' 

    
    
    #############杨辉三角这个看了别人的答案 
    ##########思路清奇 学习了
def triangle():
    L=[1]
    while 1:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
   
''''
迭代器
Iterator
''''
###

##########################
#生成器都是 Iterator 迭代器的对象
# 但是 list tuple 等都是 iterable 
#但是不是 iterator 
# 要用 iter（）函数 构造迭代器
##########################
from collections import Iterator

isinstance(iter([]),Iterator)

isinstance(iter('ABC'),Iterator)

###########################
'''
迭代器的用途和list tuple都是不相同的
因为list是在内存中开辟地址空间
而iter（）一种生成性质的函数
可以不断生成需要的数
甚至可以表示所有自然数

'''

for x in [1,2,3,4,5]:
   print(x)


####等价于
a=iter([1,2,3,4,5])
while 1:
    try:
        x=next(a)
        print(x)
    except StopIteration:
        break


