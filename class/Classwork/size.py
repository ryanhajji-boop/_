from sys import getsizeof

list = []

for i in range(1,100):
    list.append(i)
    print(i, getsizeof(list))