'''
前置和后置的方法：
模块级：setup_module(测试前置)  teardown_module(测试后置)，在模块最开始执行模块级的测试前置，在文件的末尾执行模块级的测试后置
函数级: setup_function(测试前置) teardown_function(测试后置)，函数级的测试前置和后置，在每一个测试用例的前后都执行
类级:   setup_class(self)       teardown_class(self)，在类最开始执行类级的测试前置，在文件的末尾执行类级的测试后置
方法级:  setup_method(self)     teardown_method(self)，方法级的测试前置和后置，在每一个测试用例的前后都执行

函数和方法：
    在类里面的是方法
    在类外面的是函数
'''

# 测试的前置和后置：模块级和函数级
def setup_module():
    print("测试前置：模块级，模块开始前执行")

def teardown_module():
    print("测试后置：模块级，模块开始后执行")

def setup_function():
    print("测试前置：函数级，函数开始前执行")

def teardown_function():
    print("测试后置：函数级，函数开始前执行")

def test_case001():
    print("测试用例1")
def test_case002():
    print("测试用例2")
def test_case003():
    print("测试用例3")