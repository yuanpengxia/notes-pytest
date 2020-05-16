'''
pip install pytest 安装pytest包；pip install -U pytest 更新pytest包新版本（u大小写是否都可以？---必须大写）
pytest --version 查看pytest版本号
win系统使用dir命令查看当前目录下的文件后，pytest test_simple.py执行文件
ctrl+l-----terminal清屏
pip install pytest-sugar 运行结果美化
pip install pytest-rerunfailures 重新运行出错的案例
  pytest --reruns num *.py即当运行到出错的案例时，重复给它运行num次，但程序并不停止
  pytest --reruns num --reruns-delay num2 *.py 运行到出错的案例时，重复给它运行num次并让它等待num2秒后继续执行
pip install pytest-xdist 多任务同时并发执行测试用例
pip install pytest-assume对测试用例进行添加断言(不间断的执行，会执行出所有的断言)
  脚本中加入多句pytest.assume("判断语句")
  即时第一条断言过不去，也让他继续执行并打印出断言结果，多条就执行多条断言并打印出来，且不影响脚本运行

pip install pytest-html 生成一个html页的形式的测试报告
pytest -h  查看pytest的帮助文档，查看常用功能
pytest -k  跳过不需要执行的部分案例,例如pytest -vs test_simple.py -k "Test_Demo or not test_a"代表执行符合Test_Demo*和not test_a的案例；
            pytest -vs test_simple.py -k "Test_Demo and not test_a"代表执行符合Test_Demo*和not test_a的案例
pytest -m 执行加了相同标签名称的部分案例
pytest -x 遇到错误即停止运行，例如有6跳测试用例，有2条失败，那他遇到第一条失败时就停止运行，后面的案例将不再执行
pytest --maxfail=[num]当运行错误数达到num时，脚本停止运行
pytest -v 可以详细打印测试结果信息
pytest -s 打印出所有print的内容
pytest *.py::[class名]
pytest -v test_simple.py -k "TestDemo1 and not test_a"跳过对应类下的对应模块
类Test开头，方法test_*开头（类内部外部均可）

import pytest 引用pytest包
模块级别（setuo_module/teardown_module）->函数级别（setuo_function/teardown_function）->类级别（setuo_class/teardown_class）->方法级别（setuo_method/teardown_method）(在类中)->类中（setup/teardown）运行在调用方法的前后
'''

'''
pytest-fixture的用法
场景：用例1需要先登录，用例2不需要登录，用例3需要登录，这种场景就无法使用setup和teardown来实现
应该：在需要被调用的方法前加上@pytest.fixture()

import pytest
在登录函数前加上@pytest.fixture(),参数默认scope=function
在要使用的测试方法中传入（登录函数名称），就先登录
不传入的不登录的直接执行测试方法
'''


'''
conftest文件
公用模块存放地
conftest文件可进行数据共享，并可将其放在不同位置起着不同的作用
系统执行到参数login时会在本脚本文件中查找是否有login变量的名字，然后再在conftest.py文件中找是否有此变量
最后将login模块带@pytest.fixture一并写入conftest.py
*文件名必须为conftest
*与运行文件必须在统一个package下，且有__init__.py文件
*pytest用例会自行查找,不需要导入
*全局的配置和前期工作都可以放在此文件中
'''


'''
yield关键字
已经将测试方法前要执行的或依赖的解决了，测试方法后想要销毁清除数据，属于模块级别的，类似与setupclass
即需要加入yield关键字，yield调用第一次会返回上面的结果，第二次执行yield下面的语句
在pytest.fixture(scope=module)
*在登录的方法中加yield，之后加销毁清除步骤要注意：这种方法没有返回值，如果需要返回就需要使用addfinalizer

'''
'''
fixture中参数autouse = True
不想原有测试方法有任何改用，或全部都自动实现自动应用，没特例，也都不需要返回值可以选择自动应用
在方法上加@pytest.fixture(autouse=True)
在测试方法上加@pytest.mark.usefixture("start")

'''

'''
fixture带参数传递
场景离不开数据，为了数据灵活，一般数据都是通过参数传递的，方便同样的场景不同参数的案例
fixture通过固有参数request传递
在fixture中增加@pytest.fixture(params=[1,2,'linda'])在方法参数写request

skip
此次测试不执行下面的方法
'''
'''
-m参数，执行和标记相关的所有案例
pytest -s *.py -m 方法名，例如pytest -s test_simple.py -m test就代表方法只要包含test字段，就都会被执行
'''
'''
pip install pytest-xdist
pytest-xdist:
pytest test_pytest.py -n 3
'''
'''
pytest-html生成测试报告
pip install pytest-html
生成报告执行如下：
pytest -v -s --html=report.html --self-contained-html,即生成一个report.html的测试报告文件
'''
'''
参数化
@pytest.mark.parametrize(argnames,argvalues),argname:参数变量名，可以是字符串，列表，元组；argvalues:变量对应的值，可是列表或者包含元组的列表
加载yaml文件 yaml.safe_load(open('.\*.yaml))
'''