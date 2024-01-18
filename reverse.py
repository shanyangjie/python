python_list = []
python_list.append('python')
python_list.append('izm')
python_list.append('sample')
python_list.append('list')
python_list.append('reversed')

for value in python_list:
    print(value)

# python_list.reverse()

print('---------------------------------')

# for value in reversed(python_list):
#     print(value)

for value in python_list[::-1]:
    print(value)

print('---------------------------------')

for value in python_list:
    print(value)
