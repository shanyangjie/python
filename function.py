def calc(a,b,op=1):
    if op==1:
        print(a+b)
    elif op==2:
        print(a-b)
    elif op==3:
        print(a*b)
    elif op==4:
        print(a/b)
    elif op==5:
        print(a%5)
    else:
        print("error")


print("a")
a=int(input())

print("b")
b=int(input())

print("op")
op=int(input())

calc(a,b,op)