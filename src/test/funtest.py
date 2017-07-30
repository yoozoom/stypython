# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/30 16:01


# 多个返回值
def fun_return_2(x, y):
    sts = '_fun'
    return x + sts, y + sts


# 1. 默认参数，默认参数可以不传
# 2. 固定参数在前，默认参数在后
def fun_default(x, n=4, s='-->'):
    print 'fun_default'
    print x, ' -> ', n, s


# is None
def fun_null(x):
    if x is None:
        print 'hello None'
    else:
        print x


# mul params
def fun_change_params(*a):
    i = 0
    for item in a:
        i += item
    print i


# key params
def fun_key_param(name, age, **attr):
    print name, age, attr


# 所有参数的顺序必须是必选参数、默认参数、可变参数和关键字参数
def main():
    s1 = 'kaka'
    s2 = 'messi'
    # 可以用变量分别获取
    s3, s4 = fun_return_2(s1, s2)
    print s3, s4
    # 也可以直接在一个tuple中获取
    s5 = fun_return_2(s1, s2)
    print s5

    # 默认参可以不传
    fun_default('s')
    fun_default('s', 2)
    # 如果不按定义顺序默认参数，必须显示指定参数名s=xxx
    # 编辑器中提示的为p图标
    fun_default('s', s='ok')
    fun_default(9, s="good", n=10)

    fun_null(None)
    fun_null('java')

    # *a可变个数的参数
    fun_change_params(1, 3, 4)
    fun_change_params(1, 3, 4, 6, 7)
    fun_change_params(1, 3, 4, 9, 1, 3, 1, 3, 9)
    # 集合解析成可变参数
    list1 = [1, 3, 4, 2]
    fun_change_params(*list1)

    # 关键字参数类似一个扩展的map属性
    fun_key_param('songdao', 22)
    # 自定义key value传入
    fun_key_param('songdao', 22, title='meinv', no='ipz001')
    # 直接使用map传入
    map1 = {'type': 'leg', 'title': 'teacher'}
    fun_key_param('songdao', 22, **map1)


if __name__ == '__main__':
    main()
