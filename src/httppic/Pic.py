# -*- coding:utf-8 -*-
# author yuzuo.yz 2017/7/25 21:23
import re
from hashlib import md5
from multiprocessing import Pool
from urllib import urlencode

import os
import requests
import json

from bs4 import BeautifulSoup

import pic_config as config


def get_html():
    data = {
        'offset': config.PAGE_INDEX,
        'format': 'json',
        'keyword': config.KEYWORDS,
        'autoload': 'true',
        'count': config.PAGE_SIZE,
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


def get_art(text):
    json_data = json.loads(text)
    data_list = json_data['data']
    for art_item in data_list:
        yield art_item['article_url']


def get_art_detail(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
    except Exception, e:
        print "http request error!", e
        return None


def get_art_name_img(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print title
    # re正则表达式
    img_pattern = re.compile('var gallery = (.*?);', re.S)
    rs = re.search(img_pattern, html)
    if rs:
        img_list_str = rs.group(1)
        img_list_json = json.loads(img_list_str)
        sub_images = img_list_json['sub_images']
        if sub_images:
            for sub_images_item in sub_images:
                yield sub_images_item['url']


def get_img_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
    except Exception, e:
        print "http request error!", e
        return None


def download_img(url):
    content = get_img_content(url)
    if content:
        # md5转换，md5是hashlib包下
        file_name = md5(url).hexdigest() + ".jpg"
        local_name = config.DOWNLOAD_PATH + '/' + file_name
        if not os.path.exists(local_name):
            with open(local_name, 'wb') as f:
                print "download..."
                f.write(content)


def print_json(data):
    return json.dumps(json.loads(data), indent=4)


def test_print(i):
    print i


# 开启多进程
def multi_exec(img_url):
    p = Pool(4)
    for i in range(4):
        p.apply_async(download_img, (img_url,))
    p.close()
    p.join()


def main():
    html = get_html()
    for art_url in get_art(html):
        print art_url
        detail_html = get_art_detail(art_url)

        for img_url in get_art_name_img(detail_html):
            if img_url:
                print img_url
                download_img(img_url)



if __name__ == '__main__':
    main()
