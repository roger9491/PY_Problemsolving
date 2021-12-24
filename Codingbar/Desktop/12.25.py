
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
Linked List

假設一種情況
我們維護一個串列 會時常對他進行兩種操作
(1) 查詢
(2) 插入





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
删除排序链表中的重复元素
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/submissions/

'''

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         t = []
#         temp = head
#         while temp != None:
#             number = temp.val
#             if number in t:
#                 pre.next = temp.next
#             else:
#                 t.append(number)
#                 pre = temp
#             temp = temp.next
#         return head

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


'''
圖 由 vertex 和 edge 構成

如何儲存圖?



'''

'''
相鄰矩陣表示法
範例:
5 1
1 3
1 4
2 0
2 0
3 3

有 1 , 2 , 3 , 4 , 5 點組成
'''

'''
矩陣表示法

'''

'''
樹

linked-list

'''
# class TreeNode:
#     def __init__(self,val) -> None:
#         self.val = val
#         self.left = None
#         self.right = None



'''
建立樹
我們來建立一個完全二元樹

'''
# class TreeNode:
#     def __init__(self,val) -> None:
#         self.val = val
#         self.left = None
#         self.right = None

# class function:
#     def __init__(self) -> None:
#         self.root = None
#         self.queue = []

#     def add(self,val):
#         new_node = TreeNode(val)
#         if self.root == None:
#             self.queue.append(new_node)
#             self.root = new_node
#         else:
#             parent = self.queue[0]
#             if parent.left == None:
#                 parent.left = new_node
#             elif parent.right == None:
#                 parent.left = new_node
#                 del self.queue[0]
#             self.queue.append(new_node)

# a = input().split(",")
# function = function()
# for i in a:
#     function.add(i)
'''
建立完樹 要怎麼從裡面找資料

https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
二叉树的中序遍历

用dfs 去做

'''
class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

class function:
    def __init__(self) -> None:
        self.root = None
        self.queue = []

    def add(self,val):
        new_node = TreeNode(val)
        if self.root == None:
            self.queue.append(new_node)
            self.root = new_node
        else:
            parent = self.queue[0]
            print("p",parent.val)
            if parent.left == None:
                parent.left = new_node
            elif parent.right == None:
                parent.right = new_node
                del self.queue[0]
            self.queue.append(new_node)

    def inoder(self,node):
        if self.root == None or node == None:
            return
        else:
            self.inoder(node.left)
            print(node.val)
            self.inoder(node.right)
a = input().split(",")
function = function()
for i in a:
    print("i",i)
    function.add(i)
print()
function.inoder(function.root)
'''
練習 前序 遍歷
根 -> 左子樹 -> 右子樹
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
'''


'''
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
深度練習


'''

class Solution:
    def __init__(self):
        self.temp = 0
        self.ans = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def find(node,temp):
            if node == None:
                return
            print(node.val,temp)
            temp += 1
            self.ans = max(temp,self.ans)
            find(node.left,temp)
            find(node.right,temp)
            temp -= 1

        self.ans = 0
        find(root,0)
        return self.ans

