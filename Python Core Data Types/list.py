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

M = ['bb', 'aa', 'dd', 'cc']
M.sort()  # 对列表进行排序
print(f'{M}\n')  # ['aa', 'bb', 'cc', 'dd']

M.reverse()  # 翻转列表
print(f'{M}\n')  # ['dd', 'cc', 'bb', 'aa']

# python的边界检查
# N = [1, 2, 3]
# print(f'{N[99]}\n')   IndexError: list index out of range
# N[99] = 1   IndexError: list assignment index out of range
# 避免了对内存进行危险的越界操作
