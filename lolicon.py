#-*- codeing = utf-8 -*-
import requests
import re
import time
import os
print('README!!!!!\nREADME!!!!!\nREADME!!!!!\n说明：图片返回数量，范围为1到10，不提供 APIKEY 时固定为1，只有几次测试机会\nr18参数 0为否，1为是，2为混合\n不指定关键词填0，若指定关键字，将会返回从插画标题、作者、标签中模糊搜索的结果\n是否使用 master_1200 缩略图，以节省流量或提升加载速度，0为不使用，默认不使用（玛德，没搞懂怎么用的，这玩意先不设置了）')
number = int(input('请输入要下载的图片数量：'))
if number<1 or number>10 :
    print('瞎几把输，给你一张便宜你了')
    number = 1
r18yn = int(input('是否r18：'))
if r18yn<0 or r18yn>2 :
    print('?')
    r18yn = 0
word = input('请输入图片关键词：')

if word =='0':
    word=''
# size = input('是否要压缩图片：')
# if size =='0':
#     size = 'false'
# else:
#     size =  'true'
# print(size)
data = {
    "apikey":'',  #添加apikey
    'r18':r18yn,   #添加r18参数 0为否，1为是，2为混合
    'keyword':word,   #若指定关键字，将会返回从插画标题、作者、标签中模糊搜索的结果
    'num':number,          #一次返回的结果数量，范围为1到10，不提供 APIKEY 时固定为1
    'size1200':True     #是否使用 master_1200 缩略图，以节省流量或提升加载速度
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
i = 0
d = 'D:\\B\\'
for url in url_list:
    path = d + url.split('/')[-1]
    i += 1
    print('正在下载第%d张图片' % i)

    try:

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

        print("图片获取失败")
print('图片全部下载完成')

