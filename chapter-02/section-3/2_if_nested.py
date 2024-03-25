# 示例1：检查天气和时间是否适合出去玩
weather = "晴天"
time = "下午"
if weather == "晴天":
    if time == "下午":
        print("散步的最佳时间!")
    else:
        print("稍后再去！")
else:
    print("我们还是待在室内吧。")

# 示例2：检查是否有足够的钱和时间去看电影
money = 20
free_time = True
if money >= 15:
    if free_time:
        print("我们去看电影吧！")
    else:
        print("也许下次吧。")
else:
    print("需要先存点钱。")

# 示例3：检查是否带了雨伞且外面在下雨
umbrella = True
raining = True
if raining:
    if umbrella:
        print("不用担心，我有雨伞。")
    else:
        print("哎呀，我可能会被淋湿。")
else:
    print("这是美好的一天！")