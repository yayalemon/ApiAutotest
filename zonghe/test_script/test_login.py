import pytest

from zonghe.baw import Db, Member
from zonghe.caw import DataRead, Asserts


def test_login():
    # 注册用户
    # 下发登录的请求
    # 检查结果
    # 删除注册的用户
    pass
@pytest.fixture(params=DataRead.read_yaml(r"data_case/login_data.yaml"))
def login_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml(r"data_case/login_setup.yaml"))
def setup_data(request):
    return request.param

@pytest.fixture()
def register(setup_data,url,db,baserequests):
    mobilephone=setup_data['data']['mobilephone']
    Db.delete_user(db,mobilephone)
    r=Member.register(url,baserequests,setup_data['data'])
    print(r.text)
    yield
    Db.delete_user(db,mobilephone)

def test_login2(register,login_data,url,db,baserequests):
    r=Member.login(url,baserequests,login_data['data'])
    print(r.text)
    # assert r.json()['code'] == login_data['expect']['code']
    # assert r.json()['msg'] == login_data['expect']['msg']
    # assert r.json()['status'] == login_data['expect']['status']
    Asserts.check(r.json(),login_data['expect'],'code,msg,status')