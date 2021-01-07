'''
mark标记：
1.@pytest.mark.parametrize实现参数化
2.@pytest.mark.skip/skipif  跳过用例不执行
3.@pytest.mark.func自定义的标记，实现只执行某部分用例
    接口自动化(API)、功能自动化(FUNC)、界面自动化(UI)、冒烟测试(smoke)
    通过自定义的标记，标记用例属于哪一类。
    比如版本转测，需要进行冒烟测试，执行带有冒烟测试的用例

在pytest.ini文件中配置信息如下：
    [pytest]
    addopts = -v --html=report/report.html --self-contained-html --reruns=3 -m=smoke

    markers =
        smoke: smoke test cases
        func: function test cases

配置文件中-m的参数：
    -m=smoke 执行带smoke标记的用例
    -m=func
    -m="smoke and func"执行带smoke和func标记的用例
    -m="smoke or func"执行带smoke或func标记的用例
    -m="not smoke"执行不带smoke标记的用例
'''
import pytest

version = "V1R1"
@pytest.mark.smoke()
def test_case01():
    print("用例1")


@pytest.mark.skip('跳过的原因：缺陷，改动比较大，作为以后的版本的需求来实现')
def test_case02():
    print("用例2")


@pytest.mark.skipif(version == "V1R1", reason='V1R1版本不支持，如果是v1r1版本，则跳过')
def test_case03():
    print("用例3")

@pytest.mark.func()
def test_case04():
    print("用例4")

@pytest.mark.func()
def test_case05():
    print("用例5")

#对类下面所有的用例生效
@pytest.mark.func()
class TestClass:
    @pytest.mark.smoke()
    def test_case06(self):
        print("用例6")

    @pytest.mark.smoke()
    def test_case07(self):
        print("用例7")

    def test_case08(self):
        print("用例8")

    def test_case09(self):
        print("用例9")

    def test_case10(self):
        print("用例10")

