'''
題意
有n個矩形，每一個高度都是1，且寬一定是2的x次方(任意x>=0)，
然後會有一個寬:W的2維的大箱子，(W >= 最大矩形的寬)，把所有矩形塞到
箱子裡求最小高度，只能寬朝下的塞入箱子，不能重疊、旋轉。

輸入:
第一行t(1≤t≤5*10**3)，代表接下來有幾組測資。
每一個測資有兩行，
第一行 兩個整數n(1≤n≤10**5) 矩形數, W(1≤W≤10**9)箱子寬度。
第二行 n個整數，w1,w2,w3,....wn(1≤wi≤10**6),代表n個矩形的寬度。

輸出:
t個整數代表 最小高度

example:
input:
2
5 16
1 2 8 4 8
6 10
2 8 8 2 2 8
output:
2
3

第一組測資說明:
    附圖

'''

def bs(e,target):
    for i in range(len(e)):
        if e[i] <= target:
            return i,e[i]
    return -1,-1

t = int(input())
for i in range(t):
    n,w = map(int,input().split())
    e = list(map(int,input().split()))
  
    e.sort(reverse = True)
    counter = 0
  
    while len(e) > 0:
        target = w - e[0]
        del e[0]
        #print(e)
        while target != 0:
            length = len(e)
            index,num = bs(e,target)
            if index == -1:
                counter += 1
                break
            else:
                target -= num 
                del e[index]
        else:
            counter += 1
    print(counter)