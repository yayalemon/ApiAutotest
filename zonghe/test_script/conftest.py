'''
脚本层的一些公共的方法
'''
'''
安装目录找包
如果使用IDE，会从工程的根路径开始，向下搜索
命令行执行时，当前执行的PY文件开始，向下搜索
命令行执行时，报错找不到包。解决的方法：把工程路径，放在sys.path中
'''
import sys
import os
cp=os.path.realpath(__file__)
cd=os.path.dirname(cp)
cd=os.path.dirname(cd)
cd=os.path.dirname(cd)
sys.path.append(cd)
from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests
import pytest

env_path=r"data_env/env.ini"
# 读取env.ini中的url,设置session的级别，整个执行过程只读一次
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(env_path,"url")

@pytest.fixture(scope='session')
def db():
    return eval(DataRead.read_ini(env_path,"db"))

# 创建一个BaseRequests的实例，设置session界别的，整个过程只执行一次
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()