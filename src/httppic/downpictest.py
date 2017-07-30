# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/30 14:44

import requests


def download_pic(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    response = requests.get(url, params=None, headers=headers)
    print response.status_code, response.request.headers
    content = response.content

    # with用法。对开启关闭流，或者链接类型的语法，可以代替try except finally使用。能关闭资源
    with open('1.png', 'wb') as f:
        # 一次性写入整个content
        f.write(content)


def download_pic_buffer(url):
    response = requests.get(url)
    print response.status_code

    # with用法。对开启关闭流，或者链接类型的语法，可以代替try except finally使用。能关闭资源
    with open('1.png', 'wb') as f:
        # 缓冲写入
        for item in response.iter_content(128):
            f.write(item)


def get_pic(url):
    # 设置请求后的钩子函数
    response = requests.get(url, hooks=dict(response=test_hook))
    print response.status_code


def test_hook(response, *args, **kwargs):
    print 'exec test_hook'
    print 'hook, ', response.status_code


def main():
    url = 'http://findicons.com/files/icons/2804/plex/512/python.png'
    download_pic(url)
    # download_pic_buffer(url)
    # get_pic(url)

if __name__ == '__main__':
    main()

