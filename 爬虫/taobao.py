import requests

url = "https://rate.taobao.com/feedRateList.htm?auctionNumId=559472972356&userNumId=687132834&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=098%23E1hvBpvEvbQvUpCkvvvvvjiPn2SZ6jnHR2SZtj1VPmPh1jlWRLLvljY8RLLUgjE8RsyCvvpvvvvv2QhvCPMMvvvCvpvVvvpvvhCvmphvLvp%2FWvvj7SpafX7reBlv%2BExrQ8TJnDeDyO2vHdUfbjc6D70OdeQEfwBlYb8rwk%2FQD7zZdig0747B9Wv7%2B3%2BSaNoxfXKKfvDr6jc6%2Bu0EvpvVmvvC9c3Uuphvmvvv9bF3iWRTKphv8vvvvvCvpvvvvvmvchCv2HpvvUEpphvWh9vv9DCvpvQovvmmZhCv2C85vpvhvvmv9IwCvvpvCvvv&_ksTS=1587548648444_1752&callback=jsonp_tbcrate_reviews_list"

header = {
    "cookie": "_tb_token_=xMSaBzyO73WqTqWUUnTY; _samesite_flag_=true; cookie2=1d9fc657b489f753f5e5e04fbb1c1df2; t=a64267cd3a95d1f51f18e6285461ce3c; cna=mcWJFupitQkCAXVZWNJbURMF; unb=684014105; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&nk2=tZela6y8&vt3=F8dBxGR2VDOuZWsZTlY%3D&id2=VWeV%2FjMsqePX; csg=63f1f343; lgc=%5Cu5468%5Cu6C38%5Cu9E92; cookie17=VWeV%2FjMsqePX; dnk=%5Cu5468%5Cu6C38%5Cu9E92; skt=6fcd17c14445ba90; existShop=MTU4NzU0NjUxMw%3D%3D; uc4=id4=0%40V8ZuH1nFQWrNn7IDDP5TshzSpGI%3D&nk4=0%40tyOUt2%2BtQ1w2WEM0VyQYcNE%3D; publishItemObj=Ng%3D%3D; tracknick=%5Cu5468%5Cu6C38%5Cu9E92; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=%E9%BA%9250; _nk_=%5Cu5468%5Cu6C38%5Cu9E92; cookie1=VTriwrYPYF2SLz3uV87UclT2oEZQqB20bmPf%2BCwe0XY%3D; sgcookie=EGF00J6aPye8Ogj00ZQF4; tfstk=cAqcBSwK3bOC96UbdKibB14215bdZPprM5Pb4oWqjfliyYqPiETy8u-5rbV0XF1..; mt=ci=17_1; v=0; thw=cn; uc1=cookie14=UoTUPcllLYLp0w%3D%3D&existShop=true&pas=0&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie21=UIHiLt3xSixwH1aenGbDOw%3D%3D; _m_h5_tk=afd4ba407d1d5960e05558a529d647bc_1587557628767; _m_h5_tk_enc=7af624609603422f6b36295c2dbe9e24; enc=bZeamM41IKY58t48Pw8CB978ulWCq7xKWnZfHC1rWLClUBRD%2FkByOwOfeqPkUmhhzV%2BHHZGtDMC%2BG8K7vJvKDg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; isg=BHV1JpSzR5RyvqOOsH2jTrXnhPcv8ikEaImxk_eaeew7zpTAv0NO1FQIGZJ4_0G8; l=eBTe095qQjpNJcBXBOfwourza77t-IRjhuPzaNbMiT5POYCM5CrfWZjAluTHCnhVns_XR3-y1pxLBfLnlyUMlEGfIqlBs2JZcdLh.",
    "referer": "https://item.taobao.com/item.htm?spm=a310p.7395781.1998038982.1&id=559472972356",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"

}

res = requests.get(url, headers=header)
print(res.text)