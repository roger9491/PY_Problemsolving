'''
B. WeirdSort
泡沫排序思維實戰
https://codeforces.com/problemset/problem/1311/B

題目翻譯
https://www.luogu.com.cn/problem/CF1311B

'''

t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    p = list(map(int,input().split()))

    for i in range(n-1):
        for j in p:
            j = j - 1
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

    flag = False
    for i in range(n-1):
        if a[i] > a[i+1]:
            flag = True
            break
    if flag:
        print("NO")
    else:
        print("YES")
