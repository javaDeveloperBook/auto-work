def greet(name, /, greeting="你好"):
    print(f"{greeting}，{name}！")

greet("Alice")
greet("Bob", greeting="您好")