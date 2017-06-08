# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:45:26 2017

@author: MuX

面向对象
"""
'''
面向对象的最重要的概念是明白 
类（class） 实例（instance）
概念。
牢记 ‘类’class 是抽象的模板
‘实例’ instance 是由类创建出来的一个
一个的具体的“对象”，每个对象都具有相同
的方法，但是，它们的数据功能可能是不同的

'''
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score= score
    ###__init__()函数的第一个参数
    ##永远都是self
    #self也就是说创建实例的本身
    
    #self就是一个指针？指向实例本身，
    #创建实例中的对象，
    #比如：xiaoming=Student；
    #xiaoming就是self，小明就具有了
    #name 和 score 的对象
    '''
    很重要的一点，原始的类是不给小明
    提供对象的真实世界中的意义、
    因此，小明还需要自己找“对象”在真实
    世界中的实际的名字。。。。
    xiaoming=Student(xiaoming,60)
    '''  
    #因为“类”class 本身就有数据了
    #因此，访问这些数据没有必要调用
    #外部其他的函数
    #直接在 类 中写本类的方法是 坠吼得
    def print_score(self):
        print('%s,%d'%(self.name,self.score))
    def get_grade(self):
        if self.score>90:
            return 'A'
        elif self.score<90 and self.score>60:
            return 'B'
        else:
            return 'failure'
#Python中可以在实例中加入其他的变量
#比如，加入xiaoming.age=8
#就可以调用小明.年龄，这样一个变量

#普通的类的定义太随意
#可以被外部程序改来改去
#失去了自主、独立、等等的个性
#因此，需要学习  限制访问的方法
class Student_strict(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def set_score(self,score):
        self.__score=score
    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

class Student_self(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

###加 __ 的表示的是私有变量
###加 _  的表示是私有变量，但是可以查看 不能调用

class Animal(object):
    def __init__(self):
        pass
    #####def __init__() 函数并不是必须的
    ###可以不进行定义，如果没有内容填写
    ###可以填入pass
    ##但是不能够返回 return self
    def run(self):
        print('Animal is run...')

class Dog(Animal):
    pass
#### 继承 的 多态

class Cat(Animal):
    def run(self):
        print('Cat is running...')
#Cat 继承了animal的方法
#但是，可以重新定义 cat自己的方法
#cat中定义的run（）方法就是多态
#比如 在cat中定义 cat run 在dog中定义的cat
#显示不同的东西是有意义的
class Cat(Animal):
    def run(self):
        print('Cat is running...')
    def eat(self):
        print('Cat is eating...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Dog is eating...')
cat=Cat()
dog=Dog()
cat.run()
dog.run()
cat.eat()
dog.eat()
'''
Cat is running...
Dog is running...
Cat is eating...
Dog is eating...
'''
###对于类型的解释
l=list();
a=Animal();
c=Cat();
d=Dog();

isinstance(l,list)  #true
isinstance(a,Animal) #true 
isinstance(c,Cat)  #true 
isinstance(d,Dog)  # true
 
isinstance(c,Animal) #true
isinstance(d,Animal) #true 

isinstance(c,Dog)   #false
isinstance(a,Cat)   #false

#对于多态 可以利用函数表现出优秀特性
def run_twice(Animal):
    Animal.run()
    Animal.run()
#定义一个函数，传入变量Animal类型的变量a
#再传入相同类型的变量de 实例 instance，方法可以直接调用
#并输出内容
run_twice(c)
run_twice(d)

###由于Python的动态特性
#所以不需要所有的类型都是严格根据继承过来的
class Timer(object):
    def run(self):
        print('Time is running...')

t=Timer()
run_twice(t) #依旧可以进行调用

####当拿到一个类时，确定对象是什么类型，有哪些方法
#type()函数
type(232)
type('xiaoming')

#可以使用type函数判断类型是不是相同的
type('323')==type('xiaoming')
type(a)==type(d)

#可以利用types模块中的数据类型来判断
import types
def fn():
    pass
type(fn)==types.FunctionTypes
type(abs)==types.BuiltinFunctionType
type(list())

'''
要想获得一个对象的属性和方法
'''
dir('abc')
'''
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']
'''
#__xxx__的方法都是特殊的方法
#例如调用len(‘xxx’)可以获取字符串长度，'xxx'.__len__()同样可以获取
#这两种方式是等价的

#通过getattr() setattr() hasattr()
#可以更好的对对象进行操作
class TheObject(object):
    def __init__(self,x):
        self.x=x
    def power(self):
        return self.x * self.x
        
obj=TheObject(9)
        
getattr(obj,'x')
hasattr(obj,'x')
setattr(obj,'y',10)
getattr(obj,'y')


##在Python这种动态语言中
##实例是可以绑定任意的属性的
class Student(object):
    name='xiaoming'

stu=Student()
print(stu.name)
print(Student.name)
stu.name='laowang'
print(stu.name)
del stu.name
print(stu.name)

'''
xiaoming
xiaoming
laowang
xiaoming
'''

