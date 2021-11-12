n,k = map(int,input().split())

t = input().split()

index_list = list(map(int,input().split()))
temp = "".join(t)
ans_max = 0
ans_min = 0
temp = temp.split("0")
maxv = -10**9
minv = 10**9
for i in temp:
    if "1" in i:
        maxv = max(len(i),maxv)
        minv = min(len(i),minv)
ans_max += maxv
ans_min += minv
# print(t)
for i in range(k):
    index = index_list[i]
    t[index-1] = "1"
    temp = "".join(t)
    temp = temp.split("0")
    maxv = -10**9
    minv = 10**9
    # print(temp)
    for i in temp:
        if "1" in i:
            maxv = max(len(i),maxv)
            minv = min(len(i),minv)
    ans_max += maxv
    ans_min += minv



print(ans_max)
print(ans_min)