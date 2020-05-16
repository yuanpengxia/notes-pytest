import pytest

@pytest.fixture(scope="module")#整个模块级别可用
def open():
    print("打开浏览器")
    yield
    #下面部分为运行完所有案例后执行
    print("执行teardown")
    print("最后关闭浏览器")


def test_search1(open):
    print("test_search1")

def test_search2(open):
    print("test_search2")

def test_search3(open):
    print("test_search3")


