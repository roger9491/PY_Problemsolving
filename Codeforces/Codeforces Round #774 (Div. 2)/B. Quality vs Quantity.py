'''
https://codeforces.com/contest/1646/problem/B

B. Quality vs Quantity


blue > red >= 1 
blue >= 2

2 3 4 5
3 5 5 5 6 8
'''



t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    if a.count(a[0]) == len(a) or len(a) < 3:
        print("NO")
    else:
        a.sort()
        if a[0] + a[1] < a[-1]:
            print("YES")
        else:
            left = a[0] + a[1]
            right = a[-1]
            i = 2
            j = n - 2
            flag = False
            while i <= j:
                left += a[i]
                right += a[j]
                if left >= right:
                    i += 1
                    j -= 1
                else:
                    flag = True
                    break
            if flag:
                print("YES")
            else:
                print("NO")



