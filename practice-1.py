# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:52:21 2017

@author: MuX
"""
print(r'''line1
line2
line3
''')

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print('n=',n)
print('f=',f)
print('s1=',s1,'\ns2=',s2,'\ns3=',s3,'\ns4=',s4)
print('s2=',s2)

'上海'.encode('utf-8')
len('北斗应用示范工程')  #结果是8
len('北斗应用示范工程'.encode('utf-8'))
#结果是24 utf-8的汉字是3个字节
b'\xe4\xb8\x8a\xe6\xb5\xb7'.decode('utf-8')
len(b'\xe4\xb8\x8a\xe6\xb5\xb7'.decode('utf-8'))

'Hello %s'%'world'
'Hi, %s,you have $%d'%('Lao Wang',100)
'%2d-%02d'%(2,3)  #前边空了一个格，后边补成0了
'%2d-%02d'%(2,33)

'%s,%s,%s,%s,%s'%('Lao Wang',1.5,'加特林',10000,True)  #如果不确定是什么格式的数据
#那就用%s
'growth rate: %d %%' % 7  #此处的转义字符就不能用  \  了

# -*- coding: utf-8 -*-
s1=72
s2=85
r=(s2-s1)/s1*100
print('%2.1f%%'%r)

classmates=['Laowang','Gay kun','Xiang Ge']  #长度是3
classmates[0]
classmates[1]
classmates[2]
#list的读取方式从第0位开始
classmates.append('Qiang shao')
classmates.insert(2,'Hui zong')
classmates.extend(classmates)
classmates.pop(-1)
classmates.pop(0)
classmates.remove('Xiang Ge')
classmates.count('Gay kun')
classmates.pop(1)


#classmates=('Laowang','Gay kun','Xiang Ge')
#list 定义的时候用的是[]
#tuple 定义的时候用的是 ()
#list and tuple之间的不同在于
#list可以改变
#tuple 定义之后就改变不了了

####
#tuple 改变不了的原因是：tuple的指针指向的
#对象是不改变的，因此，如果指向的是个变量
#那么变量是会发生变化的。
####
bush=2001
Obama=2008
trump=2016
president=(bush,Obama,trump)
bush=2000
#president
#(2001, 2008, 2016)
#果然，tuple定义好之后，就不能随意改变了
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

high=input('输入身高：')
weight=input('输入体重：')
bmi=int(weight)/int(high)**2
if bmi < 18.5:
    print('你太瘦了！bitch！')
elif 18.5<=bmi or bmi<25 :
    print('正常，快滚下去')
elif 25<=bmi<28:
    print('过重，微笑')
elif 28<=bmi<32:
    print('hahaha,死胖子')
else:
    print('hahaha,大肥猪，你严重肥胖了')

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello',name,'bitch')
sum=0
for i in range(100):   #range(100)输出0-99
    sum=sum+i
dic={'obama':2008,'bush':2000,'trump':2016}
dic['obama']#dictionary在访问的时候需要用[]
#Set=set([12,34,[56,78]])
Set=set([12,34,(9,[56,78])])
dic['clinton']=[1992,2000]
for president in dic:
    timelength=[dic[president],dic[president]+8 ]
    dic[president]=timelength
Set=set([12,34,56,78])
dictuple={(9,[56,78]):12,'data':34}###### it is wrong
dictuple={(9,56,78):12,'data':34}  ###### this is true






