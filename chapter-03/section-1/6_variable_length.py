def make_pizza(*toppings):
    print("正在制作披萨，加入以下配料：")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("意式辣香肠")
make_pizza("蘑菇", "青椒", "额外芝士")