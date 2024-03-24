
# 以下是一些示例代码，演示了如何使用内置函数进行不同数据类型之间的转换：

# 1. 将字符串转换为整数：
num_str = '10'
num_int = int(num_str)
print(num_int)  # 输出：10

# 2. 将整数转换为浮点数：
num_int = 10
num_float = float(num_int)
print(num_float)  # 输出：10.0

# 3. 将整数转换为字符串：
num_int = 10
num_str = str(num_int)
print(num_str)  # 输出：'10'

# 4. 将元组转换为列表：
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # 输出：[1, 2, 3]

# 5. 将列表转换为元组：
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # 输出：(1, 2, 3)

# 6. 将列表转换为集合：
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)
print(my_set)  # 输出：{1, 2, 3}

# 7. 将字典转换为列表：
my_dict = {1: 'one', 2: 'two', 3: 'three'}
my_list = list(my_dict)
print(my_list)  # 输出：[1, 2, 3]