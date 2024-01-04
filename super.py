class Parent():
    def test_method(self, msg):
        print('Parent: {}'.format(msg))

class Child(Parent):
    def test_method(self, msg):
        print('Child: {}'.format(msg))
        super().test_method(msg)

obj = Child()
obj.test_method("aaa")