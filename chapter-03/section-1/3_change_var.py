# 不可更改（immutable）对象示例
def change_number(a):
    a = 5

number = 10
change_number(number)
print(number)  # 结果仍然是10

# 可更改（mutable）对象示例
def change_list(my_list):
    my_list.append(4)

numbers = [1, 2, 3]
change_list(numbers)
print(numbers)  # 结果是[1, 2, 3, 4]