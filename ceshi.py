#-*- codeing = utf-8 -*-
#@Time : 2020/7/26 17:56
#@Author : 澪
#@File : ceshi.py
#@Software : PyCharm
import requests
import re
import time
import os
number = int(input('请输入要下载的图片数量：'))
r18yn = int(input('是否要r18，需要填1，不需要填0，混合填2：'))
word = input('请输入图片关键词：（我不知道能不能多关键词，自己试试%20或+')
size = input('是否要压缩图片，是就填True，否就填False：')

data = {
    "apikey":'600830785ec3a270d87e31',  #添加apikey
    'r18':r18yn,   #添加r18参数 0为否，1为是，2为混合
    'keyword':word,   #若指定关键字，将会返回从插画标题、作者、标签中模糊搜索的结果
    'num':number,          #一次返回的结果数量，范围为1到10，不提供 APIKEY 时固定为1
    'size1200':False     #是否使用 master_1200 缩略图，以节省流量或提升加载速度
    }

response = requests.get('https://api.lolicon.app/setu/',params=data)
html = response.text
urls1 = re.findall('url":"(.*?)"',html)
urls = str(urls1)
urls = re.sub(r'\\','',urls)
url_list = re.sub("'",'',urls)
url_list = url_list.replace('[','')
url_list = url_list.replace(']','')

url_list = url_list.strip(',').split(',')
# print(url_list)
'''
d = 'D:\\B\\'
for url in url_list:
    try:
        path = d + url.split('/')[-1]

        if not os.path.exists(d):
            os.mkdir(d)

        if not os.path.exists(path):

            r = requests.get(url)

            r.raise_for_status()

            with open(path, 'wb') as f:

                f.write(r.content)

                f.close()

                print("图片保存成功")

        else:

            print("图片已存在")

    except:

        print("图片获取失败")'''


