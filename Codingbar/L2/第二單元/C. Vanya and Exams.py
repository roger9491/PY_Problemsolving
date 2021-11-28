'''
https://codeforces.com/problemset/problem/492/C

有个有n门课程，每门课程他最多获得r学分，
他只要所有课程的平均学分等于avg，他就可以获得奖学每门课程，
他已经获得了ai学分，剩下的每个学分，都需要写bi篇论才能得到，
然后问你，最少要写多少论文才能 获得奖学金 
1<=n<=10^5;1<=avg<=10^6;1<=r<=10^9






'''




'''

n,r,avg = map(int,input().split())

now = 0
t = []
for i in range(n):
    a,b = map(int,input().split())
    t.append([b,a])
    now += a

target = avg * n
if now >= target:
    print(0)
else:
    flag = False
    ans = 0
    t.sort()
    for i in range(n):
        while t[i][1] < r:
            ans += t[i][0]
            t[i][1] += 1
            now += 1
            if now >= target:
                flag = True
                break
        if flag:
            print(ans)
            break
'''


n,r,avg = map(int,input().split())

now = 0
t = []
for i in range(n):
    a,b = map(int,input().split())
    t.append([b,a])
    now += a

target = avg * n
if now >= target:
    print(0)
else:
    flag = False
    ans = 0
    t.sort()
    # print(t,now,target)
    for i in range(n):
        if target - now <= r - t[i][1]:
            ans += (target - now)*t[i][0]
            break
        else:
            ans += (r - t[i][1])*t[i][0]
            now += (r - t[i][1])
    print(ans)