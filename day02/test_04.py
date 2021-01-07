'''
fixture（用的比较多）:
作用：
    自定义测试预制条件
    比如：用例1需要登录，用例2不需要登录，用例3需要登录，用运行的级别无法实现

优势:
    命名比较灵活，不用setup,teardown这种命名
    但不能用test_命名，这是固定的测试用例的命名
    实现数据共享，不需要import

使用：
方式一：fixture函数作为参数使用
在普通函数顶部加注释@pytest.fixture()
将fixture装饰的函数名作为参数使用

方式二：fixture函数加autouse=True修饰
在普通函数顶部加注释@pytest.fixture(autouse=True)
其他函数自动使用，autouse默认为false

方式三：fixture函数使用时加注解
在普通函数顶部加注释@pytest.fixture()
其他函数自动使用时加注解@pytest.mark.usefixtures()

yield:
    fixture的teardown操作并不是独立的函数，用yield关键字呼唤teardown
    yield不能单独存在
    yield写在fixture标记的固件中
    yield之前的代码是setup的操作，yield之后的代码是teardown的操作
    如果有异常，不影响其他用例的执行
'''
# 测试前置和后置：
import pytest

# 在普通的函数上面增加fixture的注解，表示是测试前置
@pytest.fixture()
def login():
    print("登录系统")
    yield  #yield前面是前置，后面是后置，每个方法后面都前置和后置
    print("退出登录")

# autouse=True时
# 测试用例自动使用，在每个测试用例都执行
@pytest.fixture(autouse=True)
def data():
    print("准备测试数据")

def test_query():
    print("测试查询功能，不需要登录用户登录")

# 在需要使用前置的地方，方式二：使用usefixtures注解
@pytest.mark.usefixtures('login')
def test_add():
    print("测试添加的功能，需要登录")

#在需要使用前置的地方，方式二：使用函数名作为参数
def test_delete(login):
    print("测试删除的功能，需要登录")