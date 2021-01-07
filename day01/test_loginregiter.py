'''
fixture带参数
'''
import pytest
import requests
# 登录功能的测试数据,列表中的测试数据可以是任意类型的
@pytest.fixture(params=[{"mobilephone":15006008111,"pwd":"","regname":'',"code":"20103"},
                        {"mobilephone":"","pwd":85846215,"code":"20103"},
                        {"mobilephone":"","pwd":"","code":"20103"},
                        {"mobilephone":18006007167,"pwd":"","regname":'丫丫',"code":"20103"},
                        {"mobilephone":"","pwd":"aaa58585","regname":'wawa',"code":"20103"},
                        {"mobilephone":15060715011,"pwd":"aaa55","regname":'',"code":"20108"},
                        {"mobilephone":15060715012,"pwd":"abc","regname":'丫丫',"code":"20108"},
                        {"mobilephone":15060715012,"pwd":"aaaaaa1952154126415","regname":'',"code":"20108"},
                        {"mobilephone":1,"pwd":"abc1234","regname":'',"code":"20109"},
                        {"mobilephone":136485,"pwd":"abc1234","regname":'',"code":"20109"},
                        {"mobilephone":1234567890,"pwd":"abc1234","regname":'',"code":"20109"},
                        {"mobilephone":12345678941012,"pwd":"abc1234","regname":'',"code":"20109"},
                        {"mobilephone":11111111111,"pwd":"abc1234","regname":'',"code":"20109"},
                        {"mobilephone":15006007018,"pwd":"abc1234","regname":'',"code":"20110"},
                        ])
def login_data(request): #request 是pytest中的关键字，固定的写法
    return request.param #通过request.param返回每组数据，固定的写法
# 数据驱动测试
# 登录功能的测试脚本
def test_register(login_data):
    print(f"注册功能，测试数据为：{login_data}")
    r=requests.post("http://jy001:8081//futureloan/mvc/api/member/register",login_data)
    # assert login_data['code']==r.json()["code"]
    assert r.json()["code"]==login_data['code']


@pytest.fixture(params=[{"mobilephone":15006007018,"pwd":"abc1234","code":"20111"},
                        {"mobilephone":15006007018,"pwd":"","code":"20103"},
                        {"mobilephone":"","pwd":"abc1234","code":"20103"},
                        {"mobilephone":"","pwd":"","code":"20103"},
                        {"mobilephone":123,"pwd":"123456","code":"20111"},
                        {"mobilephone":15006007018,"pwd":"12568","code":"20111"},
                        {"mobilephone":15006007018,"pwd":"1258868","code":"20111"},
                        ])
def login_data1(request): #request 是pytest中的关键字，固定的写法
    return request.param #通过request.param返回每组数据，固定的写法
# 数据驱动测试
# 登录功能的测试脚本
def test_login(login_data1):
    print(f"登录功能，测试数据为：{login_data1}")
    r=requests.post("http://jy001:8081//futureloan/mvc/api/member/login",login_data1)
    # assert login_data['code']==r.json()["code"]
    assert r.json()["code"]==login_data1['code']

@pytest.fixture(params=[{"data":{"mobilephone":15006007018,"pwd":"abc1234"},
                         "expect":{"status":0,"code":"20111","data":None,"msg":"用户名或密码错误"}},
                        {"data":{"mobilephone":15006007018,"pwd":"abc1234"},
                         "expect":{"status":0,"code":"20111","data":None,"msg":"用户名或密码错误"}}
                        ])
def login_data2(request): #request 是pytest中的关键字，固定的写法
    return request.param #通过request.param返回每组数据，固定的写法
# 数据驱动测试
# 登录功能的测试脚本
def test_login(login_data2):
    print(f"登录功能，测试数据为：{login_data2['data']}")
    r=requests.post("http://jy001:8081//futureloan/mvc/api/member/login",data=login_data2['data'])
    print(r.text)
    assert r.json()["code"]==login_data2['expect']['code']
    assert r.json()["status"]==login_data2['expect']['status']
    assert r.json()["msg"]==login_data2['expect']['msg']
