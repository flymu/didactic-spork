# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:59:00 2017

@author: MuX
"""

#####面向对象的高级用法
#__slots__
#__slots__是用在当前的  类class中作为对当前类中对象数目的限制
#
class Student(object):
    __slots__=('name','age')
    def __init__(self,name,age):
        self.name=name
        self.age=age

xiaoming=Student('xiaoming',17)

xiaoming.score=89
'''
AttributeError: 'Student' object has no attribute 'score'
'''
#因为定义了 __slots__ 所以，不可以再添加其他的对象到实例中

#但是，__slots__ 只在当前的类中定义后起作用 在子类 或其他的位置将不会起作用

class Classmate(Student):
    pass

laowang=Classmate('laowang',18)
laowang.score=87  #此时，在子类中可以加入新的对象

class Classmate(Student):
    __slots__=('score')

laowang.weight=70
'''
AttributeError: 'Classmate' object has no attribute 'weight' 此时是不能加入新的变量的
'''
#如果在子类中也定义了 __slots__ 那么，在子类中可以使用父类的__sloats__和子类本身的

class Classmate(Student):
    def __init__(self,weight):
        self.weight=weight

#如果出现在子类中进行初始化，那么传入的参数只能是子类的参数
#那么问题来了，父类的参数如何传进来？
#如果重写了__init__，为了能使用或扩展超类中的行为，最好显式的调用超类的__init__方法

### @property 装饰器
###@property装饰器是用作对传入的参数进行限制的
class Student(object):
    @property
    def score(self):
        return self.score
    
    @score.setter
    def score(self, value):
        if not isinstance(value,int):
            raise ValueError('score must ba an interger!')
        if value <0 or value>100:
            raise ValueError('score must between 0~100!')
        self._score = value
##此时，score是使用setter方法来定义的
#如果使用 getter方法，那么是一种只读的属性
class Student(object):
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self,value):
        self._birth=value
    @property
    def age(self):
        return 2017-self._birth
    
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width_value):
        if not isinstance(width_value,int):
            raise ValueError('the width must be int')
        if width_value<0 or width_value>10000:
            raise ValueError('the width must between 0-10000')
        self._width=width_value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,height_value):
        if not isinstance(height_value,int):
            raise ValueError('the height must be int')
        if height_value<0 or height_value>10000:
            raise ValueError('the height must between 0-10000')
        self._height=height_value
    @property
    def resolution(self):
        return self._height*self._width
##多重继承
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

#如果现在加上Runable 和Flyable
#的功能
class Runable(object):
    def run(self):
        print('runable')
class Flyable(object):
    def fly(self):
        print('flyable')

#此时，令Dog继承两个父类
class Dog(Mammal,Runable):
    pass

class Bat(Mammal,Flyable):
    pass

#使用MaxIn
#为了能够看出来多重继承的关系
#可以把Runable改为RunableMaxIn
#Flyable改为FlyableMaxIn
class RunableMaxIn(object):
    def run(self):
        print('runable')
class FlyableMaxIn(object):
    def fly(self):
        print('flyable')
class Dog(Mammal,RunableMaxIn):
    pass

class Bat(Mammal,FlyableMaxIn):
    pass
###定制类
#定制类有很多种
#Python中__xxxxx__这种的需要注意
#很有可能就是定制类

class Student(object):
    def __init__(self,name):
        self.name=name
print(Student('xiaoming'))

class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'this is %s'%self.name
print(Student('xiaoming'))
#如果不想写print

class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'this is %s'%self.name
    __repr__=__str__
xiaoming=Student('xiaoming')

xiaoming
class Fib(object):
    def __init__(self):
        self.a, self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000000:
            raise StopIteration
        return self.a
        
for n in Fib():
    print(n)
class Fib(object):
    def __getitem__(self,n):
        a,b=1,1
        for n in range(n):
            a,b=b,a+b
        return a 
class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for n in range(n):
                a,b=b,a+b
            return a 
        elif isinstance(n,slice):
            a,b=1,1
            start=n.start
            stop= n.stop
            if start is None:
                start=0
            L=[]
            for n in range(stop):
                L.append(a)
                a,b=b,a+b
            return L

class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    
    __repr__=__str__

class Student(object):
    def __init__(self,name):
        self._name=name
    def __call__(self):
        print('the stu is called %s'%self._name)

##在定义变量时，对常量的定义通常会
#出现问题
#引入枚举类型的 枚举类
#每个常量都是唯一的实例
from enum import Enum,unique

Month=Enum('Month',('Jan','Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6


#与静态语言不同的是
#动态语言是运行的过程中创建所有目标
#class不仅可以通过class Xxx()创建
#还可以通过type()函数进行创建
def fn(self, name='xiaoming'):
    print('Hello %s'%name)
Hello=type('Hello',(object,),dict(hello=fn))
#object后边一定要加,


#除了使用type之外，如果创建类
#还可以使用Metaclass进行对类的创建
#进行控制
#metaclass是元类
#创建元类之后
#可以由元类创建其他的类
#metaclass创建的类总是以
#Metaclass进行结尾
class ListMetaclass(type):
    def __new__(cls,name, bases, arrts):
        arrts['add']=lambda self, value:self.append(value)
        return type.__new__(cls,name,bases,arrts)

class MyList(list,metaclass=ListMetaclass):
    pass


'''
元类了解到这里，元类可以实现一些很复杂的操作
例如，实现一个ORM模型
'''
class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s>'%(self.name,self.column_type)

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
            print('Found model: %s'%name)
            mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s==>%s'%(k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings']=mappings
        attrs['__table__']=name
        return type.__new__(cls,name,bases,attrs)
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model'object has no attribute '%s'"%key)
    def __setter__(self,key,value):
        self[key]=value
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)'%(self.__table__,','.join(fields),','.join(params))
        print('SQL:%s'%sql)
        print('ARGS:%S'%str(args))
    
