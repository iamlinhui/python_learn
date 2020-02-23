# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
#
# 类的方法
# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
#
# self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
#
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。


# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.request import Request

import requests

text = requests.get(url="http://www.promptness.cn")
print(text.text)

uo = urlopen(url="http://promptness.cn")
print(uo.read().decode())

# =====================

# 处理get请求，不传data，则为get请求


url = 'http://www.xxx.com/login'
data = {"username": "admin", "password": 123456}
req_data = urlencode(data)  # 将字典类型的请求数据转变为url编码
res = urlopen(url + '?' + req_data)  # 通过urlopen方法访问拼接好的url
res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)
# 处理post请求,如果传了data，则为post请求


url = 'http://www.xxx.com/login'
data = {"username": "admin", "password": 123456}
data = urlencode(data)  # 将字典类型的请求数据转变为url编码
data = data.encode('ascii')  # 将url编码类型的请求数据转变为bytes类型
req_data = Request(url, data)  # 将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req_data) as res:
    res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)


