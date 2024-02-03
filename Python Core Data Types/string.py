# 字符串
S = 'Spam'
print(S[0])  # S
print(S[-1])  # m 等价于S[len(S)-1] 即从右偏移
print(S[1:3])  # pa 分片(slice) 从索引1开始到索引2结束 但不包括索引3
print(S[:-1])  # Spa 负偏移的作用
print(S[:])  # Spam S[0,len(s)]
print(S * 2)  # SpamSpam
print(S + 'Spam')  # SpamSpam 字符串的拼接
print('z' + S[1:])  # S[0]=z 错误 字符串是只读的
print(S[:2] + 'X' + S[2:])  # SpXam

S = 'shrubbery'
L = list(S)  # 将不可变的字符串转换为可变列表
print(L)  # ['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
L[1] = 'c'
print(L)  # ['s', 'c', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
print(''.join(L))  # join()函数 用于将序列中的元素以指定的字符连接生成一个新的字符串 此处是不用字符串连接
print(' '.join(L))  # join()函数 用于将序列中的元素以指定的字符连接生成一个新的字符串 此处是用空格连接

text = "Hello, Python"
# bytearray是Python中的一个内置数据类型，它类似于bytes对象，但具有可变性。它通常用于存储和处理二进制数据。
# B = bytearray(b'{text}') b'...'语法在3.X中必需
# B = bytearray(text.encode("utf-8")) 也可以使用 encode 方法将字符串转换为 bytearray 对象
B = bytearray(b'{text}')
B.extend(b'Project')
print(B)  # bytearray(b'Hello, PythonProject')
B[7] = ord('p')  # ord()函数以一个字符为参数，返回对应的 ASCII 数值或者 Unicode 数值
print(B)  # bytearray(b'Hello, pythonProject')
print(B.decode())  # decode() Translate to normal string

# 特定类型的方法————字符串方法，本质上是创建新串并替换，并非修改
S = 'Spam'
print(S.find('pa'))  # find方法 1 返回找到时的偏移量
print(S.find('z'))  # -1 未找到
print(S.replace('pa', 'XYZ'))  # replace方法 SXYZm
print(S.upper())  # upper()/lower() Upper-  and lowercase conversions
print(S.isalpha())  # Content tests: isalpha, isdigit, isalnum,
# isspace, istitle(Check if each word start with an uppercase letter)

line = 'aaa,bbb,ccccc,dd\n'
l1 = line.rstrip()  # Remove whitespace characters on the right side
print(l1)  # aaa,bbb,ccccc,dd
l1 = l1.split(',')  # Split on a delimiter into a list of substrings
print(l1)  # ['aaa', 'bbb', 'ccccc', 'dd']
l2 = line.rstrip().split(',')  # Combine two operations
print(l2)  # ['aaa', 'bbb', 'ccccc', 'dd']

# 格式化

print(dir(S))  # 获得帮助
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
# 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(S.replace)  # 将函数名传递给 help 函数获得其详细用法
# replace(old, new, count=-1, /) method of builtins.str instance
#     Return a copy with all occurrences of substring old replaced by new.
#
#       count
#         Maximum number of occurrences to replace.
#         -1 (the default value) means replace all occurrences.
#
#     If the optional argument count is given, only the first count occurrences are replaced.
