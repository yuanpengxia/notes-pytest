import pytest

#参数化，前两个即引号内的是变量，后面是对应的若干组数据
#3+5->test_input,8->expected
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+7",9),("7*5",30)])
def test_eval(test_input,expected):
    #eval 将字符串str即"3+5"当作有效表达式3+5来求值，并返回结果
    assert eval(test_input) == expected


#参数组合
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,10,11])
def test_foo(x,y):
    print("测试数据组合x: {x}，y: {y}")
#
#
#方法名作为参数
test_user_data = ['tom','lily']
@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 打开首页准备登录，登录用户：{user}")
    return user

#indirect=True,可以把传过来的参数当函数来执行
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
#如果不加indirect=True相当于login_r只是一个字符串而已，加上则会按照上面的方法执行
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值；{a}")
    assert a !=""
@pytest.mark.webtest
#跳过web端测试案例
@pytest.mark.android
#跳过安卓的案例
@pytest.mark.skip("此次测试不执行")
#跳过下面的案例
@pytest.mark.xfail
#标注有问题的案例，标注为xpass，不是真的pass，为测试案例预留的问题案例
@pytest.mark.parametrize("lodin_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login返回值；{a}")
    assert a !=""