'''
fixture 作用域为session级别时，
1.公共的方法放在conftest.py文件中
2.pytest是根据文件的名字找到这些方法的，不需要import。
3.当文件名不是conftest.py时，会报错test setup failed
4.测试整个文件，整个执行过程，前置和后置只执行一次
5.conftest.py 一个工程可以存在多个，对所在的目录及子目录生效
'''
import pytest
# 测试前置和后置
@pytest.fixture(scope='session')
def login():
    print("登录系统")
    yield
    print("退出登录")
