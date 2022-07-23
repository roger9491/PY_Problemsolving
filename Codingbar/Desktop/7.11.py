'''
6
3 2
3 2 1   a   2 3 1  =>    2 1 3 =>    1 2 3 
1 2     p    1 2          2 3
            p[0],p[0]+1    p[1],p[1]+1  yes

4 2
4 1 2 3     p[0],p[0]+1     p[1],p[1]+1
3 2          3 4            2       3
            4 1 2 3         4 1 2 3
NO

5 1
1 2 3 4 5
1
4 2
2 1 4 3
1 3

4 2
4 3 2 1     p[0],p[0]+1     p[1],p[1]+1
1 3          1     2        3       4       1遍p
            3 4 2 1         3 4 1 2
            p[0],p[0]+1       p[1],p[1]+1
              1     2         3       4 
            3 4 2 1         3 4 1 2 

5 2
2 1 2 3 3
1 4


YES
NO
YES
YES
NO
YES


'''

# def buble(List):
#     for i in range(len(List)-1):              0 1 2 3 4 5 ... n-1
#         for j in range(len(List)-1-i):        n-1 n-2 ...    1
#             if List[j] < List[j+1]:
#                 List[j],List[j+1] = List[j+1],List[j]
#     return(List)

# T = int(input())
# for i in range(T):
#     b = input().split()
#     Len_a = int(b[0])
#     Len_p = int(b[1])
#     a = list(map(int,input().split()))
#     p = list(map(int,input().split()))
#     c = []
#     for i in a:
#         c.append(i)
#     check = buble(a)
#     #print(c)
#     for j in range(len(p)-1):
#         c[p[j]],c[p[j+1]] = c[p[j+1]],c[p[j]]
#         if c != check:
#             print("YES")
#             break
#     else:
#         print("NO")



'''
複製串列
(1)
    c = []
    for i in a:
        c.append(i)
(2) c = a[:]    (淺複製)   
    注意 只能在一維中使用

(3) c = a.copy()

'''


'''
遇到排序的題目 一律用sort()

a.sort(reverse=True) 大到小
a.sort(reverse=True,key=sum) key:權值
int ,len, sum   :只能接收一個元素
a = ["123","234","235"]
a.sort(reverse=True,key = sum)    
print(a)

!! 背
from functools import cmp_to_key

'''

# from functools import cmp_to_key
# def f(a,b): #比較函式   a b a:121 b:456
#     if int(a+b) < int(b+a):
#         return -1   #交換 a 和 b
#     else:
#         return 1


# n = int(input())
# a = []
# for i in range(n):
#     s = input()
#     a.append(s)

# a.sort(reverse = True,key = cmp_to_key(f))
# print("".join(a))


'''
queue 佇列

a = []
加入
a.append()

拿走資料
(1)
    tmp = a[0]
    del a[0]
(2)
    tmp = a.pop(0)

'''
# a = [1,2,3,]
# tmp = a.pop(0)
# print(tmp)
# print(a)

'''
adjacency matrix
鄰接矩陣    (二維陣列)  少用
    查詢 有沒路 O(1)
         子節點 O(n)    n:節點數量
    0   1   2   3   4   5
0   1   0   1   0   1   1    
1   0   1   0   0   1   1
2   1   0   1   1   1   0
3   0   0   1   1   0   0
4   1   1   1   0   1   1
5   1   1   0   0   1   1

a:
for i in range(6):
    if a[0][i] == 1:
        print(i)

adjacency list
鄰接串列

0: 2 4 5
1: 4 5
2: 3 0 4
3: 2
4: 0 1 2
5: 0 1 4
優勢: 快速找子節點
字典
dic = {0: [2 ,4 ,5],1: [4,5]....}

串列    索引值:節點 值:子節點
a = [[2,4,5],[4,5],[],[],....]
'''
'''
bfs 廣度優先搜索

核心思想 : 擴散


dict={0:[2,3],2:[10],3:[4,5],5:[6]}

'''
# dic = {0:[2,3],2:[1,10],3:[4,5],5:[6],10:[9,11]}

# queue = [0]

# while queue:
#     node = queue.pop(0)
#     print(node)

#     if node in dic:
#         for i in dic[node]:
#             queue.append(i)

    
