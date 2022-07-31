'''
https://codeforces.com/contest/1699/problem/B

1 0 0 1 1 0         0 1 0 1 0 1 0 1
0 1 1 0 0 1         1 0 1 0 1 0 1 0
0 1 1 0 0 1         0 1 0 1 0 1 0 1
1 0 0 1 1 0         1 0 1 0 1 0 1 0

[[1,0],
 [0,1]]
[[0,1],
[1,0]]
3
2 4
2 2
4 4


1 0 0 1
0 1 1 0
1 0
0 1
1 0 1 0
0 0 1 1
1 1 0 0
0 1 0 1
'''
t = int(input())


for i in range(t):
    m1 = [['1','0'],['0','1']]
    n, m = map(int,input().split())
    a = []
    for i in range(n):
        for j in range(m//2):
            print(" ".join(m1[i%2]),end=" ")

            m1[i%2] = m1[i%2][::-1]
        
        if (i%2 == 0): print(m1)
        print()

            
        

