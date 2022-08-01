'''
https://zerojudge.tw/ShowProblem?problemid=e283
A  -> 0 1 0 1

B  -> 0 1 1 1

C  -> 0 0 1 0

D  -> 1 1 0 1

E  -> 1 0 0 0

F  -> 1 1 0 0



1
0 1 0 1
1
0 0 1 0
2
1 0 0 0
1 1 0 0
4
1 1 0 1
1 0 0 0
0 1 1 1
1 1 0 1

A
C
EF
DEBD

'''

# while True:
#     try:
#         n = int(input())
#         ans = ""

#         for i in range(n):
#             a = "".join(input().split())
#             # print(a)
#             if a == "0101":
#                 ans += "A"
#             elif a == "0111":
#                 ans += 'B'
#             elif a == "0010":
#                 ans += 'C'
#             elif a == "1101":
#                 ans += 'D'
#             elif a == "1000":
#                 ans += 'E'
#             else:
#                 ans += 'F'
#         print(ans)

#     except:
#         break

import sys

 
for j in sys.stdin:
    n = int(j)
    ans = ""

    for i in range(n):

        a = sys.stdin.readline().strip().split()
        a = "".join(a)
        # print(a)
        if a == "0101":
            ans += "A"
        elif a == "0111":
            ans += 'B'
        elif a == "0010":
            ans += 'C'
        elif a == "1101":
            ans += 'D'
        elif a == "1000":
            ans += 'E'
        else:
            ans += 'F'
    print(ans)

