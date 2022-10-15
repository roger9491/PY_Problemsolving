
# n,D=map(int,input().split())
# last=-1
# total_profit=0
# buy=0
# stock=list(map(int,input().split()))
# for i in range(n):
#     if i==0:
#        buy=stock[0]
#     else:
#         if buy!=0 and stock[i]>=buy+D:
#                 total_profit+=stock[i]-buy
#                 last = stock[i]
#                 buy=0
#         elif buy == 0 and stock[i]<=last-D:
#             buy=stock[i]           
# print(total_profit)

# n,m=map(int,input().split())
# S=list(map(int,input().split()))
# T=list(map(int,input().split()))
# idx=list(map(int,input().split()))
# l=[]
# left=[]
# for i in range(n):
#     l.append([idx[i],S[i],T[i],0])
#     left.append(i+1)
    
# while len(left)!=1:   
#     left2=left.copy()
# for i in range(1,len(left),2):
#     ab=l[left[i-1]-1][1]*l[left[i-1]-1][2]
#     cd=l[left[i]-1][1]*l[left[i]-1][2]
#     if ab>=cd:
#         l[left[i-1]-1][1]+=cd//(2*l[left[i-1]-1][2])
#         l[left[i-1]-1][2]+=cd//(2*l[left[i-1]-1][1])
#         l[left[i]-1][1]+=l[left[i]-1][1]//2
#         l[left[i]-1][2]+=l[left[i]-1][2]//2
#         l[left[i]-1][3]+=1
#         if l[left[i]-1][3]==m:
#             left2.remove(l[left[i]-1][0])
#     else:
#         l[left[i]-1][1]+=ab//(2*l[left[i]-1][2])
#         l[left[i]-1][2]+=ab//(2*l[left[i]-1][1])
#         l[left[i-1]-1][1]+=l[left[i-1]-1][1]//2
#         l[left[i-1]-1][2]+=l[left[i-1]-1][2]//2
#         l[left[i]-1][3]+=1
#         if l[left[i-1]-1][3]==m:
#             left2.remove(l[left[i-1]-1][0])
#     left=left2
# print(left[0])
'''

只剩 != 下一人
    一輪勝負

    (1) 
        重新排列
    (2)
        檢查失敗次數太多，剔除掉


'''

'''

a = [1,2,3,4]
a[2] = 5
b = [[12,3,4],[2,34,]]

建立
matrix = [[0]*n for i in range(m)]
b = [[1,4],
     [2,5],
     [3,6]]

3 2

1 2
3 4
5 6

'''
# m = 3
# n = 2
# matrix = [[0]*n for i in range(m)]
# print(matrix)
# m = []
# for i in range(3):
#     a = list(input().split())
#     m.append(a)
# print(a)

'''


輸入兩個數字 m n
建立這個 m x n 的矩陣 初始值 = (索引值相加) 判斷 
偶數 x  奇數y
印出 這矩陣


m = 4, n = 3
0+0
    [[x,y,x],
     [,,],
     [,,],
     [,,]]

ex
3 3

x y x
y x y
x y x



字串.join(串列(一維))
    合併串列
ex.
['5','3']
 
"x".join(['5','3'])
5x3
" ".join(['5','3'])
5 3
'''

# m,n=map(int,input().split())
# l=[[0]*n for i in range(m)]
# for i in range(m):
#     for j in range(n):
#         if (j+i)%2==0:
#             l[i][j]="x"
#         else:
#             l[i][j]="y"
# for i in range(m):
#     print(' '.join(l[i])) 

'''
輸入兩個數字 m n, row: m, col: n
接著輸入 m row

判斷 0的個格子 上下左右 總共有多少個1
y x

i j
上  下  左  右 重複 
i-1 i+1 j-1 j+1
j+0 j+0 i+0 i+0
上 y-1  上      下     左    右
dir = [[-1,0],[1,0],[0,-1],[0,1]]
k = [-1,0]
k = [1,0]
i j 
for k in dir:
    #方向
    a = k[0] + i
    b = k[1] + j

    #判斷有沒有超出邊界
    if 0 <= a < m and 0 <= b < n:
印出 數量

ex
2 4
0 1 1 0
1 0 1 1

7

若寫完 week2 邊緣偵測


'''


'''
實作 join()

"x".join(['1','2','3'])


輸入 串列合併的字元
輸入 一行數列

ex
y
5 8 9 0 1

5y8y9y0y1

文字
"", ''

文字相加
    + 


'''
# a = ['1','2',' ','5']
# print("y".join(a))
# pl=input()
# w=input().split()
# w2=''
# for i in range(len(w)):

#     w2+=w[i]
#     if i!=len(w)-1:
#         w2+=pl
#         break
# #w2-=pl 文字不能減
# print(w2)
a = input()
# '1 2 3 4 5'
# ['1', '2', '3', '4', '5']
print(a)

# s = ""
# # s = s +　"22"
# s += '22'
# s = '1' + s
# s += "5"
# print(s)

'''
輸入 一行字串
輸出顛倒字串

ex
abcd

dcba

1234

4321

[]
'''