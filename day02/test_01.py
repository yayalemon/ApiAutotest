'''
pytest脚本
1.文件以test_开头或者以_test结尾，一般以test_开头
2.测试类以Test开头，并且不能有init方法
3.测试函数或者方法以test_开头

需要安装的模块：pip install 模块名
pytest  测试框架
pytest-html  测试报告
pytest-xdist 多线程运行测试用例
pytest-rerunfailures 执行失败时重试
pytest-check  复合断言插件
pymysql 连接数据库
pyyaml  操作yaml文件，常用yaml来描述测试数据

命令行运行场景：
1.pytest 脚本名称.py
2.pytest 脚本名称.py --html=report.html 执行完生成测试报告
3.pytest 脚本名称.py -n NUM  多线程并发执行
    如：pytest day02\test_01.py -n 3 --reruns 2 --html=report.html
4.pytest 脚本名称.py --reruns NUM 失败重执行

命令行方式运行：
1.运行某个包下的一个模块：pytest -q 脚本名称.py
2.运行某个包下的所有模块: pytest 包名
3.运行某个方法：pytest -q 脚本名称.py::方法名
4.pytest/py.test/python -m pytest 效果一样
5.代码运行：
   if __name__ == '__main__':
      pytest.main(["-v","test_level.py"])


PyCharm默认方式运行：
File -- Setting -- Tools -- Python Integrated Tools -- Default test runner --选择pytest


'''
import requests
url="http://jy001:8081//futureloan/mvc/api/member/register"
def test_register_001():
    cs={"mobilephone":18012345678,"pwd":123456,"regname":"丫丫"}
    r=requests.post(url,data=cs)
    assert r.json()['code']=='20110'

def test_register_002():
    cs={"mobilephone":18012345678,"pwd":123456,"regname":"丫丫"}
    r=requests.post(url,data=cs)
    assert r.json()['code']=='20110'

