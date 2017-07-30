# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/29 21:50
import requests


def do_get():
    url = "http://www.baidu.com/s"
    params = {
        "wd": "python"
    }

    response = requests.get(url, params=params)
    print response.status_code
    print response.text


# 自定义request,设置url,param,headers等信息
def define_req():
    url = "http://www.baidu.com/s"
    params = {
        "wd": "python"
    }

    req = requests.Request()
    req.method = "GET"
    req.url = url
    req.headers = {'User-Agent': 'ie8'}
    req.params = params
    # requeest.prepare
    pre = req.prepare()
    print pre.headers
    print pre.method
    print pre.body
    session = requests.Session()

    response = session.send(pre, timeout=5)
    print response.text
    print response.status_code
    print response.request.url
    print response.elapsed
    print response.headers
    print response.request.headers


def main():
    define_req()

if __name__ == '__main__':
    main()