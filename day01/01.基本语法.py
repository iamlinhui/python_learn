# Python3 基础语法
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。
# 当然你也可以为源码文件指定不同的编码：

# coding=<encoding name>

# !/usr/bin/python
# -*- coding: <encoding name> -*-

# !/usr/bin/python
# vim: set fileencoding=<encoding name> :


# 注释
# Python中单行注释以 # 开头，实例如下
# 第一个注释
print("Hello, Python!")  # 第二个注释

# git init 初始化仓库
# git add . 添加文件到仓库
# git commit -m "message"  增加提交记录
# git push -u origin master 提交代码到远程分支

# 多行注释可以用多个 # 号，还有 ''' 和 """：
'''
这是注释
'''

"""
这也是注释
"""

print("你好，世界")

print(123 + 456)

a = 1 + 2 \
    + 3

print(a)

# 缩进是有意义的
print('adc\n \
        def\
ghi')

# 1.在Python中严格区分大小写
# 2.Python中的每一行就是一条语句，每条语句以换行结束
# 3.Python中每一行语句不要过长（规范中建议每行不要超过80个字符）
# 4.一条语句可以分多行编写，多行编写时语句后边以\结尾
# 5.Python是缩进严格的语言，所以在Python中不要随便写缩进
# 6.在Python中使用#来表示注释，#后的内容都属于注释，注释的内容将会被解释器所忽略
# 我们可以通过注释来对程序进行解释说明，一定要养成良好的编写注释的习惯
# 注释要求简单明了，一般习惯上#后边会跟着一个空格


# input()函数会自动识别输入内容的能力，常用于输入Number（数字）类型使用
num = input('请输入：')
print(type(num))

# 100以内奇数和
sumResult = 0
i = 1
while i <= 100:
    sumResult += i
    i += 2
print(sumResult)
