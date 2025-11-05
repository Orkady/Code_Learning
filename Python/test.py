s = input().split()

# 代码开始
'''
这是一个简单的计算器程序，用于执行基本的四则运算
程序从输入中提取两个数字和一个运算符，然后根据运算符执行相应的数学运算
支持加法(+)、减法(-)、乘法(*)和除法(/)运算
对于除法运算，会检查除数是否为零并进行相应处理
'''

# 提取操作数和运算符
num1 = int(s[0])
num2 = int(s[1])
operator = s[2]

# 根据运算符执行相应的运算
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    # 除法运算需要特别检查除数是否为零
    if num2 == 0:
        print("Divided by zero!")
    else:
        print(int(num1 / num2))
else:
    # 处理无效的运算符
    print("Invalid operator!")
# 代码结束