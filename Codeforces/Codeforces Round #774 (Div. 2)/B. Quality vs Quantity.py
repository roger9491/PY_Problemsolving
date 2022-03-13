'''
https://codeforces.com/contest/1646/problem/B

B. Quality vs Quantity


3
1 2     3 

4
5
6
....

sum(red) > sum(blue)
count(red) < count(blue)


小 ~ 大

1 2 3 4 5 6
1 + 2 + 3>=5+6
2
n - 2
'''

t = int(input())

for i in range(t):
    n = int(input())    #10**5 => nlogn=>10**5 
    a = list(map(int,input().split()))

    a.sort()
    if n == 3:
        if a[n-1] > a[0] + a[1]:
            print("YES")
        else:
            print("NO")
    else:
        #暴力法 two pointer
        if a[n-1] > a[0] + a[1]:
            print("YES")
        else:
            # print(a)
            i = 1
            j = n - 1
            blue = a[0] + a[1]
            red = a[n-1]

            while i <= j:
                if red > blue:
                    print("YES")
                    break
                i += 1
                j -= 1
  
                blue += a[i]
                red += a[j]

            else:
                print("NO")





# t = int(input())

# for i in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))

#     if a.count(a[0]) == len(a) or len(a) < 3:
#         print("NO")
#     else:
#         a.sort()
#         if a[0] + a[1] < a[-1]:
#             print("YES")
#         else:
#             left = a[0] + a[1]
#             right = a[-1]
#             i = 2
#             j = n - 2
#             flag = False
#             while i <= j:
#                 left += a[i]
#                 right += a[j]
#                 if left >= right:
#                     i += 1
#                     j -= 1
#                 else:
#                     flag = True
#                     break
#             if flag:
#                 print("YES")
#             else:
#                 print("NO")



