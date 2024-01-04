class TestClass:
    def __init__(self,num,str):
        self.num=num
        self.str=str

    
classes=[]
classes.append(TestClass(1,"aaaa"))
classes.append(TestClass(2,"bbbb"))

for cls in classes:
    print(str(cls.num)+':'+cls.str)