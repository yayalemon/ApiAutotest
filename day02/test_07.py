'''
其他：
fixture带返回值
fixture带参数，单个参数
fixture带参数：如果测试用例有多个参数，参数之间是全排列的
fixture嵌套，可以ｒｅｔｕｒｎ一个元祖、ｌｉｓｔ或字典，取各自的fixture的数据

'''
# fixture带参数
import pytest
# 登录功能的测试数据,列表中的测试数据可以是任意类型的
@pytest.fixture(params=[{"mobilephone":18012345678,"pwd":123456},
                        {"mobilephone":18012345678,"pwd":12345},
                        {"mobilephone":18012345678,"pwd":""},
                        {"mobilephone":1801,"pwd":123456}])
def login_data(request): #request 是pytest中的关键字，固定的写法
    return request.param #通过request.param返回每组数据，固定的写法
# 数据驱动测试
# 登录功能的测试脚本
def test_login(login_data):
    print(f"登录功能测试数据为：{login_data}")#格式化输出，把login_data的变量打印出来
    print(f"手机号：{login_data['mobilephone']}")
    print(f"密码：{login_data['pwd']}")