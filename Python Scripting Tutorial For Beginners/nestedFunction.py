# def func1():
#     print("This is func1")
#     x = 10
#     def func2(x):
#         print("This is func2")
#         return x + 1
#     return func2(x)

# print(func1())

# This is func1
# This is func2
# 11



# Hard Way
def func1(called_func):
    print("This is the 1st function")
    def func2(called_func):
        print("This is the 2nd function")
        called_func()
    return func2(called_func)

def func3():
    print("This is the 3rd function")

obj = func1(func3)

# This is the 1st function
# This is the 2nd function
# This is the 3rd function


# Easy Way
def func1(called_func):
    print("This is the 1st function")
    def func2(called_func):
        print("This is the 2nd function")
        called_func()
    return func2(called_func)

@func1 # Decorator
def func3():
    print("This is the 3rd function")

func3()

# This is the 1st function
# This is the 2nd function
# This is the 3rd function