'''
題目:
我們有一個序列 a，由 n + m 個的元素組合而成， ex:a1,a2,a3,....an+m 
換句話說 有一個序列 r ，個數為 n 個，ex:r1,r2,r3....rn
                  b ，個數為 m 個 ，ex:b1,b2,b3...bm
所以 a 個序列由 r 序列 和 b 序列組合而成， 而組合方式必須為
依照順序 ex : r = r1,r2,r3      b = b1,b2,b3
    合法:  a = r1,b1,r2,b2,b3,r3
    不合法: a = r2,b1,r1,r3,b2,b3
                (r1要先排)
題目希望我們排完，能從f(a) 得出最大值

f(a) = max(0,a1,(a1+a2),(a1+a2+a3),(a1+a2+a3+a4),..,(a1+a2+a3+...+a(n+m)))

輸入格式:
    第一行 t 代表 t 個側資   (1≤t≤1000) 
    每個測資的第一行 n 代表 r 序列個數  (1≤n≤100)
             第二行 r 序列      (−100≤ri≤100)
             第三行 m 代表 b 序列個數   (1≤m≤100)
             第四行 b 序列      (−100≤bi≤100)
輸出格式:
    每個測資印出最大值

example
input:
4
4
6 -5 7 -3
3
2 3 -4
2
1 1
4
10 -3 2 2
5
-1 -2 -3 -4 -5
5
-1 -2 -3 -4 -5
1
0
1
0
output:
13
13
0
0

解法:
    前綴和
詳解:
前綴和: 數列的前n項之和，ex: a = 1,2,3 前綴和 1 or 1+2 or 1+2+3
由題目希望的 求最大值的方式，我們可以知道 他是從 在求a序列 前綴和 的過程中，找出最大值，
而從 組成 a 的方式我們知道， r 與 b 的順序是不能變的 ，表示 我們在求 a的前綴和 時 也等同在 找包含r與b的前綴和，
ex:  r = r1,r2,r3      b = b1,b2,b3  
    假設 我們找完 a = r1,b1,r2,b2,b3,r3 ，
    a的前綴和 1. r1     2.r1+b1     3.r1+b1+r2      4.r1+b1+r2+b2 ....
    可以發現每一個前綴和裡都包含 r or b or r + b的前綴和
觀察出，這個規律我們可以知道 我們只要從 r 的前綴和找出最大 ，b 的前綴和找出最大 ，並把他們 做比較
    max(    0   ,   r   ,   b   ,   r+b )
           (1)     (2)    (3)       
        (1):r與b可能同時小於0
        (2):b可能是負的
        (3):r可能是負的
'''

t = int(input())

for i in range(t):
    n = int(input())
    r = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))


    pre = 0
    ans_r = -10**9
    for i in range(n):
        pre += r[i]
        ans_r = max(pre,ans_r)

    pre = 0
    ans_p = -10**9
    for i in range(m):
        pre += b[i]
        ans_p = max(pre,ans_p)

    print(max(0,ans_p,ans_r,ans_p+ans_r))