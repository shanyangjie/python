def func(name,*args):
    print(args)
    print(name)


def func1(**kwargs):
    print(kwargs)

func1(name="yangjie",address="tokyo")