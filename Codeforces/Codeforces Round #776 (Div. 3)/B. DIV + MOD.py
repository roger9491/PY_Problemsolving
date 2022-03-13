'''
https://codeforces.com/contest/1650/problem/B

5
1 4 3
5 8 4
6 10 6
1 1000000000 1000000000
10 12 8


2
4
5
999999999
5



1 + 4 = 5
2 ~ 4
4 0
'''
# t = int(input())
# for i in range(t):
#     l, r, a = map(int,input().split())
#     ans = 0
#     if a == 1:
#         print(r)
#     elif r // a > r // a - 1 + a - 1:
#         print(r//a + r%a)
#     else:
#         if r - l < a - 1:
#             if r % a >= l % a:
#                 print(r//a  + r%a)
#             else:
#                 print(r // a - 1 + a - 1)
#         else:
#             print(max(r//a+r%a, r // a - 1 + a - 1))

'''
47 // 4 = 11 + 3 = 14

'''
from random import random


def t1(l,r,a):
    b = [l,r,a]
    for i in range(a):
        c=[]
        l=b[0]
        r=b[1]
        a=b[2]
        if a>r:
            return [a,-1]
        else:
            if a==r or r%a==0:
                return [((r-1)//a+(a-1)),0]
              
            else:
                return [(r//a+r%a),1]
def t2(l,r,a):
    ans = 0
    for i in range(l,r+1):
        ans = max(i//a + i % a, ans)
    return ans
import random
while True:
    n = random.randint(1,100)
    d = random.randint(1,111)
    a = random.randint(1,100)
    print(n,n+d,a)
    ans1 = t1(n,n+d,a) 
    ans2 = t2(n,n+d,a)
    if ans1[0] != ans2:
        if a != 1:
            print("test",n,n+d,a)
            print(t1(n,n+d,a))
            print(t2(n,n+d,a))
            break