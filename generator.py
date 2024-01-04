def func_sample():
    yield('morning')
    yield('hello')
    yield('night')

# for i in func_sample():
#     print(i)

f = func_sample()
print(next(f))
print(next(f))
print(next(f))
# print(next(f))