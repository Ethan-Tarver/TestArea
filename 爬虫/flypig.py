import requests
import json
import time
import os
from urllib import parse
from urllib.parse import urljoin

# 新建一个文件夹，名字为 id+ 日期

tripid = '587497303129'
page = '1'

# 创建文件夹

data = time.strftime("%Y-%m-%d", time.localtime())
filename = tripid + "|" + data
os.mkdir('/Users/fengtingting/Downloads/python/{}'.format(filename))

# ---------默认保存到下载文件夹---------

# 定义url的查询内容，sort=1 按时间拍下
data = '?id={}&tagId=:0&pageNo={}&sort=1&pageSize=20'.format(tripid, page)


#  拼接url
url = urljoin('https://traveldetail.fliggy.com/async/queryRateList.do', data)
header = {
    "cookie":"_tb_token_=xMSaBzyO73WqTqWUUnTY; dnk=%5Cu5468%5Cu6C38%5Cu9E92; uc1=existShop=true&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=U%2BGCWk%2F7owY3j65jYmvyog%3D%3D&cookie14=UoTUPcllLCkbQQ%3D%3D; tracknick=%5Cu5468%5Cu6C38%5Cu9E92; lid=%E5%91%A8%E6%B0%B8%E9%BA%92; _l_g_=Ug%3D%3D; unb=684014105; cookie1=VTriwrYPYF2SLz3uV87UclT2oEZQqB20bmPf%2BCwe0XY%3D; login=true; cookie17=VWeV%2FjMsqePX; cookie2=1d9fc657b489f753f5e5e04fbb1c1df2; _nk_=%5Cu5468%5Cu6C38%5Cu9E92; sg=%E9%BA%9250; t=a64267cd3a95d1f51f18e6285461ce3c; csg=63f1f343; _mw_us_time_=1587546540801; cna=mcWJFupitQkCAXVZWNJbURMF; isg=BLu7RCgrYWKtUl1oOiMSDemCSpklEM8SUgsvDa1877r4DNLuNeCnYpMNJ6xCWicK; l=eBab2cVlQEXLGb8YBO5ZKurza77T6CAf5fNzaNbMiIHca1qPZQ8l_NQcDaCModtxgtC3eety4C9HvRhkJMUNixDDBej3RgOKDxvO.",
    "referer": "https://traveldetail.fliggy.com/item.htm?id=587497303129",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

res = requests.get(url, headers=header)

resdict = res.json()
# 取总条数
total = resdict['module']['rateList']['total']

# 取评价、取图片 开头：
rateCellList = resdict['module']['rateList']['rateCellList']


for i in rateCellList:

    nick = i['userNick']  # 做标题
    content = i['rateContent']  # 文本内容
    data = i['rateDate']  # 做标题
    package = i['skuInfo']  # 做标题
    # 创建一个文件夹
    contentfile = data+package+nick
    os.mkdir('/Users/fengtingting/Downloads/python/{}/{}'.format(filename, contentfile))


    # 将评价 生产text 文件 添加到自己的文件夹
    f = open("/Users/fengtingting/Downloads/python/{}/{}/{}.txt".format(filename, contentfile, content), 'a')
    f.write(content)
    f.close()

    reply = i['reply']
    pic = i['picList']
    if not pic:
        print("没有图片")
    else:
        for p in pic:
            pict = requests.get(p)
            picture = p.encode("utf-8")
            m = hashlib.md5()
            m.update(picture)
            md5_url = m.hexdigest()
            with open("/Users/fengtingting/Downloads/python/{}/{}/{}.jpg".format(filename, contentfile, md5_url),
                      'wb') as u:
                u.write(pict.content)

            # 把图片下载到对应的文件夹








# 便利第一页 20条，遍历条数+1，当条数 = total时停止
# 改page+1





