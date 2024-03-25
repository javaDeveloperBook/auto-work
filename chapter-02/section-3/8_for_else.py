# 示例：遍历列表寻找宝藏，如果没找到宝藏就放弃
treasures = ["石头", "纸", "剪刀", "黄金"]
for item in treasures:
    if item == "黄金":
        print("找到了黄金！")
        break
else:
    print("没有找到黄金。下次好运！")


# 示例：遍历列表寻找宝藏，如果没找到宝藏就放弃
treasures = ["石头", "纸", "剪刀", "宝石"]
for item in treasures:
    if item == "黄金":
        print("找到了黄金！")
        break
else:
    print("没有找到黄金。下次好运！")