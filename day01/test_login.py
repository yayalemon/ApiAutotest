import pytest
import requests

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
    r=requests.post("http://jy001:8081//futureloan/mvc/api/member/login",login_data1)
    # assert login_data['code']==r.json()["code"]
    assert r.json()["code"]==login_data1['code']