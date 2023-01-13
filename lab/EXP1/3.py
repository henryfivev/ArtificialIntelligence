n = int(input())
lis_now = [1]
for i in range(n):
    print(lis_now)
    lis_pre = lis_now
    lis_now = []
    for j in range(i+2):
        if(j != 0 and j != i+1):
            lis_now.append(lis_pre[j] + lis_pre[j-1])
        else:
            lis_now.append(1)