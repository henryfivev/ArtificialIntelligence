from itertools import count
from os import remove

from numpy import square

a = [1, 12, 11, 13, 14, 1]
b = [1, 2, 3]

a.append(3)
a.extend(b)
# print(a) [1, 12, 11, 13, 14, 1, 3, 1, 2, 3]
a.insert(0, 0)
a.remove(11)
# print(a) [0, 1, 12, 13, 14, 1, 3, 1, 2, 3]
a.pop(2)
# print(a) [0, 1, 13, 14, 1, 3, 1, 2, 3]
# a.clear()
print(a.index(13)) # 2
print(a.count(1)) # 3
# a.sort()
a.reverse()
# print(a) [3, 2, 1, 3, 1, 14, 13, 1, 0]
b = a.copy()

# stack = append() + pop()
# queue = append() + deque()

square1 = list(map(lambda x : x**2, range(10)))
square2 = [x**2 for x in range(10)]

list1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matrix1 = [[row[i] for row in matrix] for i in range(4)]
matrix2 = list(zip(*matrix))
# print(matrix2)
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

del matrix2[2:3]
# print(matrix2)
# [(1, 5, 9), (2, 6, 10), (4, 8, 12)]

tuple1 = ([1,2,3], [3,2,1])
tuple1[0][1] = 1 # ([1, 1, 3], [3, 2, 1])

#############
def fun11(a, *b):
    return 0

def fun12(a, **b):
    return 1

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")

class MyDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
#############

tuple2 = (1)
# tuple2[0] = 0
tuple_ord = (1,2,3,4)
a,b,c,d = tuple_ord
# print(a,b,c,d) 1 2 3 4

set1 = set("1,2,3,4,5,6")
dict1 = dict(a = 1, b = 2)
dict2 = {"a" : 1, "b" : 2, "c" : 3}
#print(set1) {'1', '6', '5', '4', ',', '2', '3'}
#print(dict1) {'a': 1, 'b': 2}
#print(dict2) {'a': 1, 'b': 2, 'c': 3}

for k, v in dict2.items():
    print (k, v)
for i, v in enumerate(square2):
    print (i, v)