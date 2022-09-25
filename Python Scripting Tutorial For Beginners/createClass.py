B = type("BaseClass", (object, ), {})
c1 = type("Class1", (B, ), {"val": 1})
c2 = type("Class2", (B, ), {"val": 2})

def classCreator(bool):
    if bool:
        return c1()
    else:
        return c2()

print(classCreator(True).val) # 1
print(classCreator(False).val) # 2