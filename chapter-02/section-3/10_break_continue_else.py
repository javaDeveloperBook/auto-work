# 示例1：使用break退出循环
# 这段代码会打印出0到4之间的数字。当num等于5时，break语句会使循环提前结束。
for num in range(10):
    if num == 5:
        break
    print(num)



# 示例2：使用continue跳过某些元素
# 这段代码会打印出1到9之间的奇数。当num是偶数时，continue语句会跳过当前迭代，继续执行下一次迭代。
for num in range(10):
    if num % 2 == 0:  # 偶数
        continue
    print(num)




# 示例3：使用循环的else子句
# 这段代码会打印出1、2、3。当循环结束时，如果没有触发break语句提前退出循环，那么else子句中的代码将被执行。
for num in range(1, 4):
    print(num)
else:
    print("循环已在没有使用break的情况下结束。")

