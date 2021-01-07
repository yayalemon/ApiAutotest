'''
timeout超时
1.上传文件时，上传2M耗时比较短，但是2G的文件，耗时比较久。可以使用timeout设置比较长的超时时间
2.接口测试时，测试接口的性能，但是返回的结果是否在某个时间范围内
  比如获取用户的列表的接口，是否在100ms之内
'''

import requests
url="http://jy001:8081//futureloan/mvc/api/member/list"
# requests.exceptions.ReadTimeout:
# HTTPConnectionPool(host='jy001', port=8081):
# Read timed out. (read timeout=0.001)
# r=requests.get(url,timeout=0.001)  #100ms
# print(r.text)

'''
代理 proxies
1.界面操作某个功能，结果正常，但是用自动化操作同样的功能，报错
  界面操作时，抓包
  自动化脚本执行时，抓包
  对比抓到的包，检查差异点
2.频繁的向服务器发起请求，服务器当做攻击处理，将IP地址禁了，使用代理的额IP发送请求

'''

url="http://jy001:8081//futureloan/mvc/api/member/list"
proxy={
    "http":"http://127.0.0.1:8888",#http协议，使用http://127.0.0.1:8888代理
    "https":"http://127.0.0.1:8888"
}
r=requests.get(url,proxies=proxy) #设置代理后，要把对应的代理工具Fildder打开
print(r.text)

# Https的请求，使用代理的时候，需要设置忽略证书
r=requests.get("http://www.baidu.com",proxies=proxy,verify=False)
print(r.text)