import keyword
import time

from DailyPractice import DailyPractice

print("Hello world~")

myDailyPractice = DailyPractice()

print(myDailyPractice.speed)

# 修改了myDailyPractice的属性值
myDailyPractice.say()

print(myDailyPractice.speed)

'''
 预留关键字
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
'''
print(keyword.kwlist)

"""
多行注释
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
"""
if True:
    print("True")
else:
    print("False")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")
    # 缩进不一致，会导致运行错误

'''
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。

int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''

index = 10 + 1 + \
        3 + 4
print(index)

name = "习近平" + str(index)
print(name)

numbers = ['1', '5', '10', '8']
print(numbers)

for n in numbers:
    print(n, end="", sep=".")
    print()

numbers = [int(x) for x in numbers]
print(numbers)

numbers = list(map(int, numbers))
print(numbers)


print("Loading", end="")
for i in range(20):
    print(".", end='', flush=True)
    time.sleep(0.5)

# 字符串(String)
# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# 转义符 '\'
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]


'''
标识符

第一个字符必须是字母表中字母或下划线 _ 。
标识符的其他的部分由字母、数字和下划线组成。
标识符对大小写敏感。
在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。

unicode转中文编码
python3的解决办法：字符串.encode('utf-8').decode('unicode_escape')
python2：字符串.decode('unicode_escape')
'''

fileName = '../application.properties'
try:
    file = open(fileName, mode='r')
    content = file.read()
    file.close()
    print(content.encode('utf-8').decode('unicode_escape'))
except IOError:
    print()

pro = PropertiesUtils(fileName)
configContent = pro.getProperties()
print(configContent.get("a").encode('utf-8').decode('unicode_escape'))

"""
python保留字 35个

False   True   None
and  not  or
if  else   elif  while   for  break  return  continue  in
try  except  

async  await yield 



'as', 'assert',  'class', 'def', 'del', 
'finally',  'from', 'global', 'import',  'is', 'lambda', 'nonlocal', 
'pass', 'raise',  'with', 'yield'

"""
print(len(keyword.kwlist))
print(keyword.kwlist)

"""
注释

单行注释以 # 开头

多行注释可以用多个 # 号，还有 \'\'\' 和 \"\"\"

行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
"""

"""
多行语句

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\\)来实现多行语句
"""
total = 1 + \
        2 + \
        3
print(total)

total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
print(total)

'''
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。

int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''
number = 10 / 3
print(number)

# (本金×月利率×(1＋月利率)＾还款月数)÷ ((1＋月利率)＾还款月数-1))
loanAmount = Decimal("2500")
mouthRate = Decimal("8") / Decimal("12")
print(mouthRate)

# amount = (loanAmount * mouthRate * (1 + mouthRate) ^ Decimal("12")) / ((1 + mouthRate) ^ Decimal("12") - 1))
