import pytest
import pytest_html
import yaml
def test_A():
    print("aaa")
class Test_Demo():
    def test_one(self):
        print("开始执行test_one方法")
        a = 'hello'
        assert 'h' in a
    def test_two(self):
        print("开始执行test_two方法")
        b = 'hello'
        assert 'o' in b
    def test_three(self):
        print("开始执行test_three方法")
        c = 'hello'
        d = 'hello world'
        assert c in d

class TestDemo1():
    def test_a(self):
        print("开始执行test_a方法")
        a = 'this'
        assert 't' in a

    def test_b(self):
        print("开始执行test_b方法")
        a = 'this'
        assert 'h' in a
    def test_c(self):
        print("开始执行test_c方法")
        a = 'this'
        d = 'this game'
        assert a in d
if __name__ == '__main__':
    pytest.main('-v -s --html=report.html--self-contained-html')