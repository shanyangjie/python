class TestClass:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def get(self):
        print("x:"+str(self.x)+" y:"+str(self.y))

obj= TestClass(110,4566)
obj.get()