# 示例1：基于季节推荐活动
season = "夏天"
match season:
    case "春天":
        print("现在是春天，是时候去远足了。")
    case "夏天":
        print("现在是夏天，一起去游泳吧！")
    case "秋天":
        print("现在是秋天，怎么样去看看落叶？")
    case "冬天":
        print("现在是冬天，是时候去滑雪了！")
    case _:
        print("哎呀，好像是一个未知的季节。")


# 示例2：基于成绩评定等级
grade = 85
match grade:
    case grade if grade >= 90:
        print("A")
    case grade if grade >= 80:
        print("B")
    case grade if grade >= 70:
        print("C")
    case grade if grade >= 60:
        print("D")
    case _:
        print("F")


# 示例3：基于动物发出相应的声音
animal = "猫"
match animal:
    case "狗":
        print("汪汪")
    case "猫":
        print("喵喵")
    case "鸟":
        print("啾啾")
    case _:
        print("未知动物")