# 列表（list）用中括号
# 元组（tuple）用圆括号
# 注意除注释与字符串外，一般情况下要使用英文符号！
import numpy as np


x = [4, 'haha', True, 1.3, np.sin]
print(x)
print(type(x))  # 打印类型
print(len(x))  # 打印长度（包含几个元素）

print(x[1])  # 打印列表中的第1号元素
print(x[1:3])  # 打印列表中的第1到2号元素

# 用+号拼接两个列表
y = [2, 0]
z = x + y
print(z)

# numpy函数库可以同时计算列表中元素对应的数学函数值
# 例：打印出从0到9所有整数的sin值
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(np.sin(x))


"""
练习：
1. 等差数列列表的生成（在之后学习的for循环中很常用）
  a. 搜索引擎搜索并自学python编程中“range”命令的说明与用法
  b. 打印出list(range(10))
  c. 利用list(range(10))，计算并打印出从0到9所有整数的sin值
2. 定义元素为4, 3, 2, 1的元组，并参考列表的操作，完成下列操作
  a. 打印元组的第2号元素
  b. 将该元组与元组('a', 'b')拼接
  c. 打印拼接后元组的长度（len），打印结果应为6
  d. 打印拼接后元组的第2至4号元素，打印结果应给出2, 1, 'a'
提示：列表和元组有很多类似的地方，在很多情况下可以任选其一使用
3. 通过搜索引擎，尝试列出1条list和tuple的区别，并编程测试这种区别
  例如：不能通过赋值改变tuple中元素的值，而list可以
  代码测试：
    x = [1, 2, 3]
    x[0] = 5
  上述代码不会报错，并成功将x的0号元素赋值为5
    x = (1, 2, 3)
    x[0] = 5
  上述代码报错：TypeError: 'tuple' object does not support item assignment
"""




