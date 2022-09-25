class Demo:

    @classmethod
    def class_method(cls):
        print("Class method called")
    
    @staticmethod
    def static_method():
        print("Static method called")
    
    def instance_method(self):
        print("Instance method called")

Demo.class_method()
Demo.static_method()
Demo.instance_method(Demo())

# Class method called
# Static method called
# Instance method called

class Dec:
    @classmethod
    def addOne(self, x):
        return x + 1
    
    @staticmethod
    def addTwo(x):
        return x + 2

print(Dec.addOne(10)) # 11
obj = Dec()
print(obj.addTwo(10)) # 12