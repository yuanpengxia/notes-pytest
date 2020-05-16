import pytest

#module优先最高，最先执行
def setup_module():
    print("这是一个setup_module方法")

#最后执行
def teardown_module():
    print("这是一个teardown_module方法")


def setup_function():
    print("这是一个setup_function方法")

def test_login():
    print("这是一个外部的方法")


def teardown_function():
    print("这是一个setup_function方法")


class TestDemo():
    def setup_class(self):
        print("setup_class")
    def test_one(self):
        print("test_one")

    def setup_method(self):
        print("setup_method")
    def test_two(self):
        print("test_two")

    def teardown_method(self):
        print("teardown_method")

    def teardown_class(self):
        print("teardown_class")
