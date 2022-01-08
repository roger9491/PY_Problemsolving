'''
歷史考卷分數

'''
# n = int(input())
# s1 = input().split()
# temp = [0]*(n)
# for i in range(n):
#     temp[int(s1[i]) - 1] = str(i+1)
# s1 = temp
# # print(s1)
# while True:
#     try:
#         s2 = input().split()
#         temp1 = [0]*(n)
#         for i in range(n):
#             temp1[int(s2[i]) - 1] = str(i+1)
#         s2 = temp1

#         dp = [[0]*(len(s1)+1) for i in range(len(s2)+1)]

#         for i in range(1,len(s2)+1):
#             for j in range(1,len(s1)+1):
#                 if s1[j-1] == s2[i-1]:
#                     dp[i][j] = max(dp[i][j-1],dp[i-1][j-1]+1)   #因為 當前一樣 上一次的前一個肯定沒有當前的+1
#                 else:
#                     dp[i][j] = max(dp[i][j-1],dp[i-1][j])
#                     # dp[i][j] = dp[i][j-1]
#         print(dp[-1][-1])
#     except:
#         break

'''
分組背包
https://www.luogu.com.cn/problem/P1757
3 5
2
1 2
2 4
1
3 4
1
4 5 

8

'''

# m,n = map(int,input().split())

# item = {}
# for i in range(n):
#     a = list(map(int,input().split()))
#     if a[2] not in item:
#         item[a[2]] = [[a[0],a[1]]]
#     else:
#         item[a[2]].append([a[0],a[1]])
# # print(item)
# # dp = [[0]*(m + 1) for i in range(len(item))]
# # print(len(dp))
# index = 0
# # for i in item:
# #     for j in range(m + 1):
# #         maxv = -10**9
# #         w = 0
# #         for x in item[i]:
# #             if j >= x[0]:
# #                 if maxv < x[1]:
# #                     maxv = x[1]
# #                     w = x[0]
# #         dp[index][j] = max(dp[index-1][j],dp[index-1][j-w] + maxv)
# #     # print(dp[index])
# #     index += 1
# dp = [0]*(m + 1)
# for i in item:
#     for j in range(m,-1,-1):
#         maxv = -10**9
#         w = 0
#         for x in item[i]:
#             if j >= x[0]:
#                 if maxv < x[1]:
#                     maxv = x[1]
#                     w = x[0]
#         dp[j] = max(dp[j],dp[j-w] + maxv)
#     # print(dp[index])
# # print(dp)
# print(dp[-1])



'''
相鄰領地


'''

# def bfs(i,j):
#     queue = [[i,j]]
#     path[i][j] = 1
#     count = 0
#     direction = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
#     while queue:
#         node = queue.pop(0)
#         count += 1
#         for r in direction:
#             i_next = node[0] + r[0]
#             j_next = node[1] + r[1]
#             if 0 <= i_next < n and 0 <= j_next < m:
#                 if matrix[i_next][j_next] == 0 and path[i_next][j_next] == 0:
#                     queue.append([i_next,j_next])
#                     path[i_next][j_next] = 1
#     return count


# m,n = map(int,input().split())

# matrix = []
# for i in range(n):
#     e = list(map(int,input().split()))
#     matrix.append(e)


# path = [[0]*m for i in range(n)]
# ans = []
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] == 0 and path[i][j] == 0:
#             ans.append(bfs(i,j))

# ans.sort()
# ans = list(map(str,ans))
# print(" ".join(ans))

'''
01矩陣

'''
# def bfs(i,j):
#     queue = [[i,j]]
#     path = [[0]*m for i in range(n)]
#     path[i][j] = 1
#     count = 0

#     while queue:
#         size = len(queue)    
#         while size:
#             node = queue.pop(0)
#             if matrix[node[0]][node[1]] == "0":
#                 return count
#             for r in dire:
#                 i_next = node[0] + r[0]
#                 j_next = node[1] + r[1]
#                 if 0 <= i_next < n and 0 <= j_next < m:
#                     if path[i_next][j_next] != 1:
#                         queue.append([i_next,j_next])
#                         path[i_next][j_next] = 1
#             size -= 1
#         count += 1
    


# n,m = map(int,input().split())

# matrix = []

# for i in range(n):
#     e = input().split()
#     matrix.append(e)

# ans = [[0]*m for i in range(n)]
# dire = [[0,1],[1,0],[-1,0],[0,-1]]

# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] == "1":
#             ans[i][j] = bfs(i,j)

# for i in range(n):
#     ans[i] = list(map(str,ans[i]))
#     print(" ".join(ans[i]))


'''
class

'''



# class people(): #模板
#     def __init__(self,val,next): #初始化
#         self.val = val
#         self.next = None

    # def print1(self):
    #     print(self.h)
    #     print(self.w)

    

# p1 = people(200,100)
# head = p1
# print(p1)

# #記憶體位置不同
# # print(id(p1),id(p2))
# p1.print1()



# a = 1
# b = a
# print(id(a),id(b))
#認為變數的不同 代表本體的不同

#值才是物體












# class role():
#     def __init__(self) -> None:
#         self.name = "asda"
#         self.occup = "animal"
#     def print(self,name):
#         print("123")
#         print(name)
# slime = role()
# slime2 = role()
# slime.print(123)
# print(id(slime))
# print(id(slime2))
# print(slime)
'''
Linked List

假設一種情況
我們維護一個串列 會時常對他進行兩種操作
(1) 查詢
(2) 插入

(1)新增節點在頭

''' 
# class node():   #節點定義
#   def __init__(self,val):
#       self.val = val    #資料
#       self.next = None  #下一個

# class function():
#     def __init__(self):    #定義 頭
#         self.head = None
        
#     def add_head(self,val):     #新增節點在頭
#         new_node = node(val)    #2
#         if self.head == None:
#             self.head = new_node
#             return
#         new_node.next = self.head

'''
新增節點1  2
寫個function 印出節點1的資料，並且head指向節點1


'''


        









'''
建立linked-list
寫一個class- function 新增節點在頭
                      遍歷節點印出
'''

# class node():
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# class function():
#     def __init__(self) -> None:
#         self.head = None    #頭指標

#     def add_head(self,data):
#         new_node = node(data)

#         temp = self.head
#         self.head = new_node
#         new_node.next = temp

#     def traverse_list(self):
#         temp = self.head
#         while temp != None:
#             print(temp.data)
#             temp = temp.next

# link_function = function()

# link_function.add_head(1)
# link_function.add_head(2)
# link_function.add_head(3)

# link_function.traverse_list()

'''
建立linked-list
寫一個class- function 新增節點在頭
                      遍歷節點印出
                      插入第i個節點
'''

# class node():
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# class function():
#     def __init__(self) -> None:
#         self.head = None    #頭指標

#     def add_head(self,data):
#         new_node = node(data)

#         temp = self.head
#         self.head = new_node
#         new_node.next = temp

#     def add_i_node(self,i,data):
#         temp = self.head
#         count = 0
#         while count < i - 1:
#             count += 1
#             temp = temp.next
#         temp2 = node(data)
#         temp2.next = temp.next
#         temp.next = temp2

#     def traverse_list(self):
#         temp = self.head
#         while temp != None:
#             print(temp.data)
#             temp = temp.next

# link_function = function()

# link_function.add_head(1)
# link_function.add_head(2)
# link_function.add_head(3)

# link_function.traverse_list()

# link_function.add_i_node(1,4)
# link_function.traverse_list()


'''
https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
刪除特定節點

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def deleteNode(self, head: ListNode, val: int) -> ListNode:
#         temp = head
#         pre = None
#         while head != None and head.val != val:
#             pre = head
#             head = head.next
#         if pre:
#             pre.next = head.next 
#         else:
#             temp = head.next
#         return temp

'''
https://leetcode-cn.com/problems/reverse-linked-list/
反轉鏈表

'''
# class node():
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# class function():
#     def __init__(self) -> None:
#         self.head = None    #頭指標

#     def add_head(self,data):
#         new_node = node(data)

#         temp = self.head
#         self.head = new_node
#         new_node.next = temp

#     def add_i_node(self,i,data):
#         temp = self.head
#         count = 0
#         while count < i - 1:
#             count += 1
#             temp = temp.next
#         temp2 = node(data)
#         temp2.next = temp.next
#         temp.next = temp2

#     def traverse_list(self):
#         temp = self.head
#         while temp != None:
#             print(temp.data)
#             temp = temp.next

#     def reverseList(self) :
#         head = self.head
#         head2 = head
#         temp = head.next
#         head.next = None
#         head = temp
#         while head != None:
#             temp = head.next
#             head.next = head2
#             head2 = head
#             head = temp
#             print(head2.data)
#             print(head) 
#         head = head2
# link_function = function()

# link_function.add_head(4)
# link_function.add_head(3)
# link_function.add_head(2)
# link_function.add_head(1)

# link_function.traverse_list()
# print("start")
# link_function.reverseList()

# link_function.traverse_list()


# 新增節點1  2
# 寫個function 印出節點1的資料，並且head指向節點1
# (1)新增節點在頭

class node():   #模板
    def __init__(self,val):
        self.val = val
        self.next=None  #指向下一格節點

class function1():
    def __init__(self):
        self.head=None

    # def head_to_node1(self,node):   #head_to_node1 head指向節點1
    #     self.head = node
    #     print(self.head.val)
    #     print(node.val)
    #     print(self.head)
    #     print(node)
    def add_to_head(self,val):  #
        new_node = node(val)    #建立節點
        
        if self.head == None:
            self.head = new_node
        else:   #若 有一個以上節點時
            new_node.next = self.head
            self.head = new_node
    
    def traverse_linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.val)
            temp = temp.next


function1 = function1()
function1.add_to_head(100)
function1.add_to_head(200)
function1.add_to_head(300)
function1.traverse_linked_list()
