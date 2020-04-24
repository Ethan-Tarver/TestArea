import requests
import json

url = "https://traveldetail.fliggy.com/async/queryRateList.do?id=587497303129&tagId=:0&pageNo=1&sort=0&pageSize=20"
header = {
    "cookie":"_tb_token_=xMSaBzyO73WqTqWUUnTY; dnk=%5Cu5468%5Cu6C38%5Cu9E92; uc1=existShop=true&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=U%2BGCWk%2F7owY3j65jYmvyog%3D%3D&cookie14=UoTUPcllLCkbQQ%3D%3D; tracknick=%5Cu5468%5Cu6C38%5Cu9E92; lid=%E5%91%A8%E6%B0%B8%E9%BA%92; _l_g_=Ug%3D%3D; unb=684014105; cookie1=VTriwrYPYF2SLz3uV87UclT2oEZQqB20bmPf%2BCwe0XY%3D; login=true; cookie17=VWeV%2FjMsqePX; cookie2=1d9fc657b489f753f5e5e04fbb1c1df2; _nk_=%5Cu5468%5Cu6C38%5Cu9E92; sg=%E9%BA%9250; t=a64267cd3a95d1f51f18e6285461ce3c; csg=63f1f343; _mw_us_time_=1587546540801; cna=mcWJFupitQkCAXVZWNJbURMF; isg=BLu7RCgrYWKtUl1oOiMSDemCSpklEM8SUgsvDa1877r4DNLuNeCnYpMNJ6xCWicK; l=eBab2cVlQEXLGb8YBO5ZKurza77T6CAf5fNzaNbMiIHca1qPZQ8l_NQcDaCModtxgtC3eety4C9HvRhkJMUNixDDBej3RgOKDxvO.",
    "referer": "https://traveldetail.fliggy.com/item.htm?id=587497303129",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

data = {"id": 587497303129, "tagId": 0, "pageNo": 1", "sort": "0", "pageSize": "20"}




res = requests.get(url, params=data, headers=header,)

# print(res.json())
print(res.rul)