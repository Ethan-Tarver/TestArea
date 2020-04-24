import requests
import json
import urllib
from urllib import parse

# "https://traveldetail.fliggy.com/async/queryRateList.do?id=587497303129&tagId=:0&pageNo=1&sort=0&pageSize=20"

res = parse.urlparse("https://traveldetail.fliggy.com/async/queryRateList.do?id=587497303129&tagId=:0&pageNo=1&sort=0&pageSize=20")
print(res.query)