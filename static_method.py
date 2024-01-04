class Test:

    @staticmethod
    def add(x,y):
        return x+y
    
print(Test.add(3,7))

obj=Test()
print(obj.add(3,9))