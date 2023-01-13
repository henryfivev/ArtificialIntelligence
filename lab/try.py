from copy import copy

listrange = list(range(10))
print(listrange)


def ui():
    print('----')
    print('--------命题逻辑归结推理系统--------')
    print('----')
    
ali = [('name',123),('dwded',3233)]
a = set(ali)

l = [[1, 3], [2, 4]]
if ([1, 3] in l):
    print ("[] in l")
a.add(())
sea = [["0", 1, 2], "0", ["1", 3, 4]]
if "0" in sea:
    print("find 0") # wont be into
if ali.index(111) == -1:
    print(ali.index)
aa = list(a)
a.add(('fedfs',123))
print(aa[-1])
ll = ['123', '213','343']

for x in ll:
    for y in ll:
        x6 = copy.deepcopy(x)
        y6 = copy.deepcopy(y)
        x = '222z'
        y = 000
b = set()
b.add({'www':321})
if a == b:
    print("a == b")

if a in b :
    print("a in b")
else :
    print("a not in b")

print("hello")