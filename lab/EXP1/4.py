class Mylist:
    def __init__(self, *l):
        self.mylist = list(l)

    def push_list(self, args):
        self.mylist.append(args)
    def get(self, num):
        if(num > len(self.mylist)):
            num = len(self.mylist)
        for i in range(num):
            print(self.mylist[i], end=" ")
    def len_list(self):
        print(len(self.mylist))
    def del_list(self):
        self.mylist = self.mylist[1:]
        print(self.mylist)
    def clear_list(self):
        self.mylist = []

t = Mylist([1,2,3,"asd"])
print("after __init__:",t.mylist)
t.push_list("iop")
print("after push_list_str:",t.mylist)
t.push_list(999)
print("after push_list_int:",t.mylist)
print("after get:", end="")
t.get(4)
print("\nafter len_list:", end="")
t.len_list()
t.del_list()
print("after del_list:", t.mylist)
t.clear_list()
print("after clear_list:", t.mylist)