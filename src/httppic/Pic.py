# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/25 21:23
from urllib import urlencode

import requests
import json


def get_html():
    data = {
        'offset': 0,
        'format': 'json',
        'keyword': '美女',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3
    }
    url = 'https://www.toutiao.com/search_content/'
    # url = 'https://www.toutiao.com/search_content/?' + urlencode(data)

    try:
        response = requests.get(url, params=data)
        # response = requests.post(url, data=data) 使用post方式提交表单 application/x-www-form-urlencoded
        # response = requests.post(url, json=data) 使用ajax方式提交    application/json

        if response.status_code == 200:
            # c = response.json()['count'] 可以直接获取json中的数据
            # c = response.json()['count']
            # print "test count", c

            # print response.request.headers
            print response.request.url

            return response.text
    except Exception, e:
        print "http request error!", e
        return None


def build_url(url, endpoint):
    return "/".join([url, endpoint])


def print_json(data):
    print data
    return json.dumps(json.loads(data), indent=4)


def main():
    html = get_html()
    print print_json(html)

    # test method
    # print build_url("http://www.baidu.com", "hello")
    # test json
    # test_str = '{"name":"kaka", "age": 10, "fav":{"name":"football","title":"play"}}'
    # print print_json(test_str)


if __name__ == '__main__':
    main()
