'''
https://www.luogu.com.cn/problem/P1102
P1102 A-B 数对


'''

n, c = map(int,input().split())

a = list(map(int,input().split()))

dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
# print(dic)
ans = 0
# print(dic)
for i in dic:
    if i + c in dic:
        ans += dic[i]*dic[i+c]
    # if i - c in dic:
    #     ans += max(dic[i],dic[i-c])

    # print(ans)
print(ans)

'''
1 2
2 3 
1 2

'''