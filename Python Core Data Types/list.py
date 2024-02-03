L = [123, 'spam', 1.23]
print(f'{len(L)}\n')

L.append('NI')
print(f'{L}\n')

L.insert(1, 'eggs')
print(f'{L}\n')

print(L.pop())
print(f'{L}\n')

print(L.pop(1))
print(f'{L}\n')

L.remove('spam')
print(f'{L}\n')


