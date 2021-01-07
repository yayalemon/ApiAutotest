'''
注册的测试脚本
'''
from zonghe.baw import Member, Db
from zonghe.caw import DataRead
import pytest
import requests


# pytest数据驱动的方式
# 从yaml中读取测试数据
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_pass.yaml"))
def pass_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_repeat.yaml"))
def repeat_data(request):
    return request.param

# 注册失败的脚本
def test_register_fail(url,baserequests,fail_data):
    # 下发注册的请求
    r=Member.register(url,baserequests,fail_data['data'])
    print(r.text)
    # 断言结果
    assert r.json()['code']==fail_data['expect']['code']
    assert r.json()['msg']==fail_data['expect']['msg']
    assert r.json()['status']==fail_data['expect']['status']

# 注册成功的脚本
def test_register_pass(url,baserequests,pass_data,db):
    mobilephone = str(pass_data['data']['mobilephone'])
    Db.delete_user(db,mobilephone)
    r=Member.register(url,baserequests,pass_data['data'])
    assert r.json()['code'] == pass_data['expect']['code']
    assert r.json()['msg'] == pass_data['expect']['msg']
    assert r.json()['status'] == pass_data['expect']['status']
    # 调用查询的接口，在查询的结果中能找到本次注册的手机号
    h=Member.querylist(url,baserequests)
    assert mobilephone in h.text
    Db.delete_user(db,mobilephone)

def test_register_repeat(url,baserequests,repeat_data,db):
    mobilephone = str(repeat_data['data']['mobilephone'])
    Member.register(url, baserequests, repeat_data['data'])
    r = Member.register(url, baserequests, repeat_data['data'])

    assert r.json()['code'] == repeat_data['expect']['code']
    assert r.json()['msg'] == repeat_data['expect']['msg']
    assert r.json()['status'] == repeat_data['expect']['status']
    # 清理环境
    Db.delete_user(db, mobilephone)