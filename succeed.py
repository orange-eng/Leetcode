
# python
# author orange
# Date 2021/5/16


# 类的继承关系和多态关系


class Animal():
    def __init__(self,name):
        self.name = name
        self.age = 10
    def greet(self):
        print("Hello I am an %s."% self.name)

class Dog(Animal):  
    #继承了animal 类中的初始化部分
    def greet(self):
        print("Wang Wang I am %s." % self.name)
        print(" My age is %s." %self.age)

class Cat(Animal):  
    #继承了animal 类中的初始化部分
    def greet(self):
        print("Wang Wang I am %s." % self.name)
        print(" My age is %s." %self.age)

#-------------------多态
# 传递的参数是一个父类，在调用时依然可以使用子类
def hello(Animal):
    Animal.greet()

dog = Dog("dog")
hello(dog)
cat = Cat("cat")
hello(cat)


# -------------------------------迭代

class Fib():
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):     #定义之后,Fib函数可以迭代
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a +self.b
        return self.a

fib = Fib()
for i in fib:
    if i > 10:
        break
    print(i)