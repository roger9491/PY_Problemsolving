'''
圖 graph

vertex
edge

無向圖/有向圖

如何儲存?
鄰接矩陣    adjacency matrix
    0   1   2   3
0   -1  1   -1   1
1   1  -1   1   -1
2  -1   1   -1  -1
3   1   -1  -1  -1

鄰接串列    adjacency list


dict = {0:[1,3],1:[0,2],2:[1],3:[0]}



'''


'''
dic={0:2,2:50,50:100}
'''

# def f(n):
#     if n == 10:
#         return
#     print(n)
#     f(n+1)
# f(1)

# def run(n):
#     if n not in dic:
#         return
#     else:
#         print(n)
#         return run(dic[n])  #retrun 子節點
# dic={0:2,2:50,50:100}
# run(0)

'''
dic = {0:[2],2:[4,8],8:[7,100]}

'''

# dic = {0:[2],2:[4,8],8:[7,100]}

# def run(n): #0  2
#     print(n)
#     if n not in dic:
#         return
#     else:
#           #0  2
#         for i in dic[n]:  #4,8
#             run(i)  #retrun 子節點
# run(0)
# dict={0:[2],2:[4,8],8:[7,10]}
# def a(n):
#     if n not in dict:
#         return
#     else:
#         print(n)
#         for i in dict[n]:
#             if i in dict:
#                 return a(i)
#             else:
#                 print(i)
# a(0)

'''
dict={0:[2,3],2:[10],3:[4,5],5:[6]}
遍歷所有的點
'''

# dict={0:[2,3],2:[10],3:[4,5],5:[6]}
# def a(n):   #a(0)   a(3)
#     print(n)
#     if n not in dict:
#         return
#     else:
#         for i in dict[n]:#2,3
#             a(i)    #a(3)

# a(0)

'''
dfs 深度優先搜索

核心思想 : 模仿人類走路


dict={0:[2,3],2:[10],3:[4,5],5:[6]}
承上題 印出 0 到 葉節點的路徑
'''
# dic = {0:[2,3],2:[10],3:[4,5],5:[6]}

# def f(n):
#     temp.append(n)
#     if n not in dic:
#         print(temp)
#         return
#     else:
#         for i in dic[n]:
#             f(i)
#             del temp[-1]
        
# temp = []
# f(0)
# print(temp)
'''
有向圖

改無向圖
遍歷

dict={0:[2,3],2:[10],3:[4,5],5:[6],2:[10,0]}
'''

# dic = {0:[2,3],2:[0,10],3:[4,5],5:[3,6],10:[2],4:[3],6:[5]}

# def f(n):   #0  2
#     print(n)
#     record.append(n)
#     for i in dic[n]:    #2,3    0,10
#         if i not in record:
#             f(i)    
# record = []
# f(0)

'''
0 1
1 2
0 5
1 4
2 3
5 4
4 3
5 6
4 7
3 8
6 7
7 8


dic[key] = value
if key in dic:
'''
dic = {}
for i in range(12):
    a,b = map(int,input().split())
    if a in dic:
        dic[a].append(b)
    else:
        dic[a]=[b]
    if b in dic:
        dic[b].append(a)
    else:
        dic[b]=[a]
def f(n):
    print(n)
    record.append(n)
    for i in dic[n]:
        if n not in record:
            f(i)
record = []
f(0)
