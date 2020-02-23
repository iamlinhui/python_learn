# Python3 运算符

---

## 什么是运算符？

本章节主要说明Python的运算符。举个简单的例子  `4 +5 = 9` 。
例子中，**4** 和 **5** 被称为操作数，"**+**" 称为运算符。

Python语言支持以下类型的运算符:

- [算术运算符](#ysf1)
- [比较（关系）运算符](#ysf2)
- [赋值运算符](#ysf3)
- [逻辑运算符](#ysf4)
- [位运算符](#ysf5)
- [成员运算符](#ysf6)
- [身份运算符](#ysf7)
- [运算符优先级](#ysf8)

接下来让我们一个个来学习Python的运算符。

---

## Python算术运算符

以下假设变量a为10，变量b为21：

|运算符|描述|实例|
|-----|---|---|
|+|加 - 两个对象相加| a + b 输出结果 31|
|-|减 - 得到负数或是一个数减去另一个数| a - b 输出结果 -11|
|*|乘 - 两个数相乘或是返回一个被重复若干次的字符串| a * b 输出结果 210|
|/|除 - x 除以 y b / a 输出结果 2.1%取模 - 返回除法的余数 |b % a 输出结果 1|
|**|幂 - 返回x的y次幂 |a**b 为10的21次方|
|//|取整除 - 向下取接近除数的整数|9//2 = 4  -9//2 = -5|

以下实例演示了Python所有算术运算符的操作：

## 实例(Python 3.0+)
```python
#!/usr/bin/python3
a = 21
b = 10
c = 0
c = a + b
print("1 - c 的值为：", c)
c = a - b
print("2 - c 的值为：", c)
c = a * b
print("3 - c 的值为：", c)
c = a / b
print("4 - c 的值为：", c)
c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print("6 - c 的值为：", c)
a = 10
b = 5
c = a//b
print("7 - c 的值为：", c)
```

```text
以上实例输出结果：

1- c 的值为：31
2- c 的值为：11
3- c 的值为：210
4- c 的值为：2.1
5- c 的值为：1
6- c 的值为：8
7- c 的值为：2
```

---

## Python比较运算符

以下假设变量a为10，变量b为20：

|运算符|描述|实例|
|-----|-----|-----|
| `==` | 等于 - 比较对象是否相等| (a == b) 返回 False。 |
| `!=` | 不等于 - 比较两个对象是否不相等| (a != b) 返回 True。|
| `>` | 大于 - 返回x是否大于y |(a > b) 返回 False。|
|  `<` | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。 |(a < b) 返回 True。 |
| `>=` | 大于等于 - 返回x是否大于等于y。 |(a >= b) 返回 False。|
| `<=` | 小于等于 - 返回x是否小于等于y。| (a <= b) 返回 True。|
 
以下实例演示了Python所有比较运算符的操作：

## 实例(Python 3.0+)

#!/usr/bin/python3a = 21b = 10c = 0if(a == b):
   print("1 - a 等于 b")else:
   print("1 - a 不等于 b")if(a != b):
   print("2 - a 不等于 b")else:
   print("2 - a 等于 b")if(a < b):
   print("3 - a 小于 b")else:
   print("3 - a 大于等于 b")if(a > b):
   print("4 - a 大于 b")else:
   print("4 - a 小于等于 b")# 修改变量 a 和 b 的值a = 5;
b = 20;
if(a <= b):
   print("5 - a 小于等于 b")else:
   print("5 - a 大于  b")if(b >= a):
   print("6 - b 大于等于 a")else:
   print("6 - b 小于 a")

以上实例输出结果：

    1- a 不等于 b
    2- a 不等于 b
    3- a 大于等于 b
    4- a 大于 b
    5- a 小于等于 b
    6- b 大于等于 a

---

## Python赋值运算符

以下假设变量a为10，变量b为20：
运算符描述实例=简单的赋值运算符 c = a + b 将 a + b 的运算结果赋值为 c+=加法赋值运算符 c += a 等效于 c = c + a-=减法赋值运算符 c -= a 等效于 c = c - a*=乘法赋值运算符 c *= a 等效于 c = c * a/=除法赋值运算符 c /= a 等效于 c = c / a%=取模赋值运算符 c %= a 等效于 c = c % a**=幂赋值运算符 c **= a 等效于 c = c ** a//= 取整除赋值运算符 c //= a 等效于 c = c // a:=海象运算符，可在表达式内部为变量赋值。**Python3.8 版本新增运算符**。
在这个示例中，赋值表达式可以避免调用 len() 两次:

    if(n := len(a))>10:print(f"List is too long ({n} elements, expected <= 10)")

以下实例演示了Python所有赋值运算符的操作：

## 实例(Python 3.0+)

#!/usr/bin/python3a = 21b = 10c = 0c = a + bprint("1 - c 的值为：", c)c += aprint("2 - c 的值为：", c)c *= aprint("3 - c 的值为：", c)c /= aprint("4 - c 的值为：", c)c = 2c %= aprint("5 - c 的值为：", c)c **= aprint("6 - c 的值为：", c)c //= aprint("7 - c 的值为：", c)

以上实例输出结果：

    1- c 的值为：312- c 的值为：523- c 的值为：10924- c 的值为：52.05- c 的值为：26- c 的值为：20971527- c 的值为：99864

---

## Python位运算符

按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：

下表中变量 a 为 60，b 为 13二进制格式如下：

    a =00111100
    
    b =00001101-----------------
    
    a&b =00001100
    
    a|b =00111101
    
    a^b =00110001~a  =11000011

运算符描述实例&按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 (a & b) 输出结果 12 ，二进制解释： 0000 1100| 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 (a | b) 输出结果 61 ，二进制解释： 0011 1101^按位异或运算符：当两对应的二进位相异时，结果为1  (a ^ b) 输出结果 49 ，二进制解释： 0011 0001~ 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1 (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。<<左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。 a << 2 输出结果 240 ，二进制解释： 1111 0000>>右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数  a >> 2 输出结果 15 ，二进制解释： 0000 1111
以下实例演示了Python所有位运算符的操作：

## 实例(Python 3.0+)

#!/usr/bin/python3a = 60# 60 = 0011 1100 b = 13# 13 = 0000 1101 c = 0c = a & b;        # 12 = 0000 1100print("1 - c 的值为：", c)c = a | b;        # 61 = 0011 1101 print("2 - c 的值为：", c)c = a ^ b;        # 49 = 0011 0001print("3 - c 的值为：", c)c = ~a;           # -61 = 1100 0011print("4 - c 的值为：", c)c = a << 2;       # 240 = 1111 0000print("5 - c 的值为：", c)c = a >> 2;       # 15 = 0000 1111print("6 - c 的值为：", c)

以上实例输出结果：

    1- c 的值为：122- c 的值为：613- c 的值为：494- c 的值为：-615- c 的值为：2406- c 的值为：15

---

<span>|</span>

## Python逻辑运算符

Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
运算符逻辑表达式描述实例andx and y 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。   (a and b) 返回 20。orx or y布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。 (a or b) 返回 10。notnot x布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 not(a and b) 返回 False 
以上实例输出结果：

## 实例(Python 3.0+)

#!/usr/bin/python3a = 10b = 20if(aandb):
   print("1 - 变量 a 和 b 都为 true")else:
   print("1 - 变量 a 和 b 有一个不为 true")if(aorb):
   print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")else:
   print("2 - 变量 a 和 b 都不为 true")# 修改变量 a 的值a = 0if(aandb):
   print("3 - 变量 a 和 b 都为 true")else:
   print("3 - 变量 a 和 b 有一个不为 true")if(aorb):
   print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")else:
   print("4 - 变量 a 和 b 都不为 true")ifnot(aandb):
   print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")else:
   print("5 - 变量 a 和 b 都为 true")

以上实例输出结果：

    1-变量 a 和 b 都为true2-变量 a 和 b 都为true，或其中一个变量为true3-变量 a 和 b 有一个不为true4-变量 a 和 b 都为true，或其中一个变量为true5-变量 a 和 b 都为false，或其中一个变量为false

---

## Python成员运算符

除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
运算符描述实例in
如果在指定的序列中找到值返回 True，否则返回 False。 x 在 y 序列中 , 如果 x 在 y 序列中返回 True。not in如果在指定的序列中没有找到值返回 True，否则返回 False。x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
以下实例演示了Python所有成员运算符的操作：

## 实例(Python 3.0+)

#!/usr/bin/python3a = 10b = 20list = [1, 2, 3, 4, 5];
 
if(ainlist):
   print("1 - 变量 a 在给定的列表中 list 中")else:
   print("1 - 变量 a 不在给定的列表中 list 中")if(bnotinlist):
   print("2 - 变量 b 不在给定的列表中 list 中")else:
   print("2 - 变量 b 在给定的列表中 list 中")# 修改变量 a 的值a = 2if(ainlist):
   print("3 - 变量 a 在给定的列表中 list 中")else:
   print("3 - 变量 a 不在给定的列表中 list 中")

以上实例输出结果：

    1-变量 a 不在给定的列表中 list 中2-变量 b 不在给定的列表中 list 中3-变量 a 在给定的列表中 list 中

---

## Python身份运算符

 
身份运算符用于比较两个对象的存储单元
运算符描述实例is
is 是判断两个标识符是不是引用自一个对象**x is y**, 类似 **id(x) == id(y)** , 如果引用的是同一个对象则返回 True，否则返回 Falseis notis not 是判断两个标识符是不是引用自不同对象** x is not y** ， 类似 **id(a) != id(b)**。如果引用的不是同一个对象则返回结果 True，否则返回 False。 
**注：**[id()](/python/python-func-id.html) 函数用于获取对象内存地址。

以下实例演示了Python所有身份运算符的操作：

## 实例(Python 3.0+)

#!/usr/bin/python3a = 20b = 20if(aisb):
   print("1 - a 和 b 有相同的标识")else:
   print("1 - a 和 b 没有相同的标识")if(id(a) == id(b)):
   print("2 - a 和 b 有相同的标识")else:
   print("2 - a 和 b 没有相同的标识")# 修改变量 b 的值b = 30if(aisb):
   print("3 - a 和 b 有相同的标识")else:
   print("3 - a 和 b 没有相同的标识")if(aisnotb):
   print("4 - a 和 b 没有相同的标识")else:
   print("4 - a 和 b 有相同的标识")

以上实例输出结果：

    1- a 和 b 有相同的标识2- a 和 b 有相同的标识3- a 和 b 没有相同的标识4- a 和 b 没有相同的标识

> is 与 == 区别：
> 
> is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
> 
> 
> 
> >>>a = [1, 2, 3]
> >>> b = a
> >>> bisaTrue
> >>> b == aTrue
> >>> b = a[:]
> >>> bisaFalse
> >>> b == aTrue

---

## Python运算符优先级

以下表格列出了从最高到最低优先级的所有运算符：
运算符描述**指数 (最高优先级)~ + -按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)* / % //乘，除，求余数和取整除+ -加法减法>> <<右移，左移运算符&位 'AND'^ |位运算符<= < > >=比较运算符== !=等于运算符= %= /= //= -= += *= **=赋值运算符is is not身份运算符in not in成员运算符not and or逻辑运算符
以下实例演示了Python所有运算符优先级的操作：

## 实例(Python 3.0+)

#!/usr/bin/python3a = 20b = 10c = 15d = 5e = 0e = (a + b) * c / d#( 30 * 15 ) / 5print("(a + b) * c / d 运算结果为：",  e)e = ((a + b) * c) / d# (30 * 15 ) / 5print("((a + b) * c) / d 运算结果为：",  e)e = (a + b) * (c / d);    # (30) * (15/5)print("(a + b) * (c / d) 运算结果为：",  e)e = a + (b * c) / d;      #  20 + (150/5)print("a + (b * c) / d 运算结果为：",  e)

以上实例输出结果：

    (a + b)* c / d 运算结果为：90.0((a + b)* c)/ d 运算结果为：90.0(a + b)*(c / d)运算结果为：90.0
    a +(b * c)/ d 运算结果为：50.0

and 拥有更高优先级:

## 实例

x = Truey = Falsez = Falseifxoryandz:
    print("yes")else:
    print("no")

以上实例输出结果：

    yes

> **注意：**Pyhton3 已不支持 <>  运算符，可以使用 != 代替，如果你一定要使用这种比较运算符，可以使用以下的方式：
> 
>     >>>from __future__ import barry_as_FLUFL
>     >>>1<>2True

---

    x =True
    y =False
    z =Falseif x or y and z:print("yes")else:print("no")

    x =True
    y =False
    z =Falseifnot x or y:print(1)elifnot x ornot y and z:print(2)elifnot x or y ornot y and x:print(3)else:print(4)

[课后练习](#)

第 1 题，共 7 题

x 的 y 次方(xy) 以下表达式正确的是?

- [x^y](#)
- [x**y](#)
- [x^^y](#)
- [Python 没有提到](#)

 22 % 3 表达式输出结果为？

- [7](#)
- [1](#)
- [0](#)
- [5](#)

3*1**3 表达式输出结果为？

- [27](#)
- [9](#)
- [3](#)
- [1](#)

9//2 表达式输出结果为？

- [1](#)
- [2](#)
- [3](#)
- [4](#)

如果表达式的操作符有相同的优先级，则运算规则是？

- [左到右](#)
- [右到左](#)
- [看心情](#)

    x =True
    y =False
    z =Falseif x or y and z:print("yes")else:print("no")

以上代码输出结果为？

- [yes](#)
- [no](#)
- [编译出错](#)

    x =True
    y =False
    z =Falseifnot x or y:print(1)elifnot x ornot y and z:print(2)elifnot x or y ornot y and x:print(3)else:print(4)

以上代码输出结果为？

- [1](#)
- [2](#)
- [3](#)
- [4](#)

[下一题](#)[完成](#)[重新测验](#)

$(function() {
code1= '<pre>' + $("#py-qa-1").html() + '</pre>';
code2= '<pre>' + $("#py-qa-2").html() + '</pre>';
  $('#quiz').quiz({
    counterFormat: '第 %current 题，共 %total 题',
    resultsFormat: '回答正确 %score 题，总共 %total 题！',
    nextButtonText: '下一题',
    finishButtonText: '完成',
    restartButtonText: '重新测验',
    questions: [
      {
        'q':  'x 的 y 次方(x<sup>y</sup>) 以下表达式正确的是?',
        'options': [
          'x^y',
          'x**y',
          'x^^y',
          'Python 没有提到'
        ],
        'correctIndex': 1,
        'correctResponse': '回答正确。',
        'incorrectResponse': '回答错误，正确的是 x**y。'
      },
      {
        'q':  ' 22 % 3 表达式输出结果为？',
        'options': [
          '7',
          '1',
          '0',
          '5'
        ],
        'correctIndex': 1,
        'correctResponse': '回答正确。',
        'incorrectResponse': '回答错误，正确的是 1.'
      },
      {
        'q':  '3*1**3 表达式输出结果为？',
        'options': [
          '27',
          '9',
          '3',
          '1'
        ],
        'correctIndex': 2,
        'correctResponse': '回答正确。',
        'incorrectResponse': '回答错误，正确的是 3。** 拥有更高的优先级。'
      },
      {
        'q': '9//2 表达式输出结果为？',
        'options': [
          '1',
          '2',
          '3',
          '4'
        ],
        'correctIndex': 3,
        'correctResponse': '回答正确，// 用于向下取接近除数的整数。',
        'incorrectResponse': '回答错误，正确的为 4，// 用于向下取接近除数的整数。'
      },
      {
        'q': '如果表达式的操作符有相同的优先级，则运算规则是？',
        'options': [
          '左到右',
          '右到左',
          '看心情',
        ],
        'correctIndex': 0,
        'correctResponse': '回答正确。',
        'incorrectResponse': '回答错误，正确的为左到右。'
      },
      {
        'q': code1 + '<p>以上代码输出结果为？</p>',
        'options': [
          'yes',
          'no',
          '编译出错'
        ],
        'correctIndex': 0,
        'correctResponse': '回答正确，and 拥有更高优先级，会先行运算。',
        'incorrectResponse': '回答错误，and 拥有更高优先级，会先行运算。'
      },
      {
        'q': code2 + '<p>以上代码输出结果为？</p>',
        'options': [
          '1',
          '2',
          '3',
          '4'
        ],
        'correctIndex': 2,
        'correctResponse': '回答正确，优先级顺序为 NOT、AND、OR。',
        'incorrectResponse': '回答错误，优先级顺序为 NOT、AND、OR。'
      },
    ]
  });
})