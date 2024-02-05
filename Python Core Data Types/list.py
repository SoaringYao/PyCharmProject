# print(*objects, sep=' ', end='\n', file=None, flush=False) 由此可知，python的print函数默认用空格分隔每个对象，并以换行符结尾

L = [123, 'spam', 1.23]
print(f'{len(L)}\n')

L.append('NI')
print(f'{L}\n')
# [123, 'spam', 1.23, 'NI']

L.insert(1, 'eggs')
print(f'{L}\n')
# [123, 'eggs', 'spam', 1.23, 'NI']

print(L.pop())
# NI
print(f'{L}\n')
# [123, 'eggs', 'spam', 1.23]

print(L.pop(1))
# eggs
print(f'{L}\n')
# [123, 'spam', 1.23]

L.remove('spam')
print(f'{L}\n')  # [123, 1.23]
