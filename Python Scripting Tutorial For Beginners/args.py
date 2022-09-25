def func(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(key, value)
    
    for i in kwargs.items():
        print(i)

func(1, 2, 3, a = 10, b = 20, c = 30)
# 1
# 2
# 3
# a 10
# b 20
# c 30
# ('a', 10)
# ('b', 20)
# ('c', 30)