# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/26 20:38

# dict 字典map构建函数
jsonObj = dict(name="kaka", age=10, title="player")
# 类似json赋值的方式构建dict对象
dict2 = {
    'name': 'messi',
    'age': 22
}

print jsonObj
print dict2

print type(jsonObj)
print dir(jsonObj)
print type(dict2)
print dir(dict2)

a = dict()
a["a"] = "b"

print a

a2 = {"name" : "juliy"}
a2["age"] = 22

print a2
print type(a2)
print dir(a2)
