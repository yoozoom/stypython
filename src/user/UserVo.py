# -*- coding:utf-8 -*-
class UserVo(object):
    # 新写法继承object可以获得object的自带属性和方法,且type为自己声明的类型
    # 老写法不继承object只有自己定义的属性和方法，且type为默认的instance类型
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        print "father init..."

    def say(self):
        print "hello my name is ", self.name;

    def get_age(self):
        return self.age

    @classmethod
    def say_hello(cls):
        print "hello! This is static method!"


class Teacher(UserVo):
    def __init__(self, name, age, title):
        # 调用父类构造函数使用super(子类名, self),__init__调用不使用self声明
        super(Teacher, self).__init__(name, age);
        print "sub init..."
        self.title = title;

    def say(self):
        print self.title, "-", self.name, " is coming ", self.age;


# test
u = UserVo("jesscia", 22);
u.say();
print dir(u);
print type(u);
print u.age;
print u.__dict__
print u.__doc__
UserVo.say_hello();


print "=================================================="

t = Teacher("haitian", 23, "s1-no1");
t.say();
print t.age
print dir(t);
print type(t);
print isinstance(t, UserVo);
print isinstance(t, Teacher);
print issubclass(Teacher, UserVo);
