def calculator():
    """
    简单计算器函数
    支持基本的四则运算：加法(+)、减法(-)、乘法(*)、除法(/)
    """

    try:
        # 获取用户输入并分割成列表
        user_input = input("请输入计算表达式（例如：5 3 +）: ").split()

        # 检查输入是否包含三个元素
        if len(user_input) != 3:
            print("输入格式错误！请按照 '数字1 数字2 运算符' 的格式输入，如：5 3 +")
            return

        # 提取操作数和运算符
        operand1_str, operand2_str, operator = user_input

        # 尝试转换字符串为数字
        try:
            num1 = float(operand1_str)  # 使用float以支持小数运算
            num2 = float(operand2_str)
        except ValueError:
            print("输入的不是有效数字！")
            return

        # 根据运算符执行相应的运算
        if operator == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operator == "/":
            # 除法运算需要特别检查除数是否为零
            if num2 == 0:
                print("错误：除数不能为零！")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        elif operator == "//":  # 整除运算
            if num2 == 0:
                print("错误：除数不能为零！")
            else:
                result = num1 // num2
                print(f"{num1} // {num2} = {result}")
        elif operator == "%":  # 取余运算
            if num2 == 0:
                print("错误：除数不能为零！")
            else:
                result = num1 % num2
                print(f"{num1} % {num2} = {result}")
        elif operator == "**":  # 幂运算
            result = num1 ** num2
            print(f"{num1} ** {num2} = {result}")
        else:
            # 处理无效的运算符
            print(f"无效的运算符 '{operator}'！支持的运算符有：+, -, *, /, //, %, **")

    except Exception as e:
        print(f"发生未知错误：{e}")


def main():
    """
    主函数，运行计算器程序
    """
    print("=" * 40)
    print("         欢迎使用简单计算器")
    print("    支持运算符：+, -, *, /, //, %, **")
    print("    输入格式：数字1 数字2 运算符")
    print("    示例：5 3 + 或 10 2.5 *")
    print("=" * 40)

    while True:
        try:
            calculator()

            # 询问是否继续计算
            continue_calc = input("\n是否继续计算？(y/n): ").lower().strip()
            if continue_calc not in ['y', 'yes', '是']:
                print("感谢使用计算器，再见！")
                break
            print()  # 添加空行以改善输出格式

        except KeyboardInterrupt:
            print("\n\n程序被用户中断，再见！")
            break
        except Exception as e:
            print(f"程序发生错误：{e}")
            break


# 如果直接运行此脚本，则执行主函数
if __name__ == "__main__":
    main()