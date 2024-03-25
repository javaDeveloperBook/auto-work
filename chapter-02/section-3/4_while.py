# 示例1：吃糖果直到罐子空了
candies = 5
while candies > 0:
    print(f"吃掉一个糖果。剩余糖果数量：{candies}")
    candies -= 1

# 示例2：计数到5
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# 示例3：等待用户输入正确的密码
password = ""
while password != "magic":
    password = input("请输入密码：")
    if password == "magic":
        print("密码正确！")
    else:
        print("密码错误，请重试。")