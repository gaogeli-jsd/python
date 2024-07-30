# lambda式は、sorted(), map(), filter()などの関数
#  に渡す無名関数として利用されることがあります。

a = [1, 2, 3]
print(list(map(lambda x: x ** 2, a)))       #=> [1, 4, 9]