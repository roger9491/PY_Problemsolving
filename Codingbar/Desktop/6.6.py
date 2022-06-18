a = [1,2,3,4,5]

print(a[0:4:2])
print(a[4:0:1])
'''
間隔 > 0
起點 < 末項

a = [1,2,3,4,5,6,7,8,9]
     0 1 2 3 4 5 6 7 8
輸入 一行
起點 末項 間隔

實作 a[首項:末項:間隔] 功能
a[1:5:1]
不能用 a[首項:末項:間隔]
輸出
串列


ex
(1)
1 5 1

[23,-1,2,15]
print(b[1:5:1])
(2)
1 7 2

[23,2,]
int()
函式一定是接小括號()
'''
# b = [1,23,-1,2,15,23,45,32]

# a = input()
# a = a.split()
# a = list(map(int,a))
# print(a)
# for i in a:
#     d.append(int(i))
# a = d
# e = []
# for i in range(a[0],a[1],a[2]):
#     e.append(b[i])
# print(e)
    
'''
https://leetcode-cn.com/problems/reshape-the-matrix/
複習 二維矩陣
'''



'''

獲得 在串列裡這個值得索引值


a = [23,1,2,3,6,1,56,8]

輸入一個數字

輸出 數字在a裡的索引值
    如果不在a裡印出-1

ex
1.
23

0

2.
1

1

3.
56

6


時間複雜度 ?
n**2    n!

2 3
n**2  >  n!

n >= 4
n**2  <  n!


不理會 常數次數
只在意 變數次數

為什麼要學會判斷時間複雜度?
(1) 時間越短越好，能知道如何改善程式碼

(2) 由時間複雜來判斷，寫出的程式碼有沒有符合出題人的規定
    由時間複雜來判斷，出題人要考的演算法 和 資料結構

EX. len(a) == 1000 => 1000*1000 => 10**6
len(a) == 10000 => 10000*10000 => 10**8
今天 oj 有時間上的規定， 原則上 c c++ : 1s， py : 3s
c/c++/py : 10**6~7  基準判斷
10**5 

10**8
情況壞
(1) 你要找的資料剛好在最後一個
(2) 你要找的資料不再串列
why? 
    因為你都要把串列裡的每個值都跑一遍
所以你的時間就是根據你[串列的長度]所決定的
                        n
時間複雜度O(n)

'''
# a = [23,1,2,3,6,1,56,8] #O(1)
# b = int(input())    #O(1)
# for i in range( len(a) ):   #O(n) + O(n)
#     if a[i] == b:   #O(1)
#         print(i)    #O(1)
#         break   #O(1)
# else:
#     print(-1)   #O(1)
'''
O(1) +　O(1)　＋　O(n) + O(n)*(O(1))
O(n+n+2) = O(2n+2) ==> O(n)


'''

# a = [23,1,2,3,6,1,56,8]
# print(a.index(1))
'''
實作 max() 變化版 

輸入 一列數列

輸出 最大的整數,索引值

ex
1 9 8 67 32 

67 3

-1 -9 -8 -67 -32 

儲存最大值的變數 初始值?

(1) 設值極值
    (1) float("inf") 無限大 -float("inf")無限小
    (2) 10**9               -10**9
(2) 設置串列的第一項

'''

a = list(map(int,input().split()))
yee = -10000
for i in range(len(a)):
    if yee < a[i]:
        yee = a[i]
print(yee)


a = [1,9,8,67,32 ]
print(max(a))


'''
最遙近的距離

判斷時間複雜度


(1) 暴力法

(2) 先 sort ， 再處理   O(nlogn)
    1.串列.sort()   改動原本的串列
    2.sorted(串列)  不會改動原本的串列


時間複雜度 ?
n**2    n!

2 3
n**2  >  n!

n >= 4
n**2  <  n!


不理會 常數次數
只在意 變數次數

為什麼要學會判斷時間複雜度?
(1) 時間越短越好，能知道如何改善程式碼

(2) 由時間複雜來判斷，寫出的程式碼有沒有符合出題人的規定
    由時間複雜來判斷，出題人要考的演算法 和 資料結構

EX. len(a) == 1000 => 1000*1000 => 10**6
len(a) == 10000 => 10000*10000 => 10**8
今天 oj 有時間上的規定， 原則上 c c++ : 1s， py : 3s
c/c++/py : 10**6~7  基準判斷

'''
# (1) O(n**2) 一組測資
# n=int(input())

# for i in range(n):
#     a=input().split()   #O(1)
#     a=list(map(int,a))  #O(1)
#     c=float("inf")      #O(1)

#     for j in range(len(a)): #O(n)   
#         for i in range(j+1,len(a)): #O(n)   O(n**2)
#             if abs(a[i]-a[j])<c: #O(1)
#                 c=a[i]-a[j] #O(1)

#     print(c)

# (2) O(n**2) 
# n = int(input())

# for i in range(n):
#     a = list(map(int,input().split()))
#     c = 10**34000

#     a.sort()

#     for j in range(len(a)-1):   # O(n)
#         if a[j+1]-a[j]<c:
#             c = a[j+1]-a[j]
#     print(c)


'''
Bubble sort
時間複雜度 O(n**2)

    排序數列 

ex  產生隨機數列

import random   #匯入 模組
a = []
for i in range(5):
    a.append(random.randint(1,30))  #random.randint(1,30) 產生1 ~ 30 數字

print(a)
'''
# import random
# a = []
# for i in range(5):
#     a.append(random.randint(1,30))
# print(sorted(a))    #用sorted()來排序 跟 下面寫的程式碼 做比對
# for k in range(len(a)-1): #len(a) * (len(a) - 1)  O(n*(n-1)) => O(n**2)
#     for j in range(len(a)-1-k):
#         if a[j]>a[j+1]:
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1]=temp
# print(a)


'''
B. WeirdSort
泡沫排序思維實戰
https://codeforces.com/problemset/problem/1311/B

題目翻譯
https://www.luogu.com.cn/problem/CF1311B


[[1,2,3,4]]

1 3 5 7 9


13256
13311

12 321 12 213 


6
3 2     n , m
3 2 1   a   a[1] a[2] 2 3 1     a[1] a[2] 1 2 3
1 2     p   a[2] a[3] 2 1 3  
4 2
4 1 2 3     2 3     3 4
3 2
5 1
1 2 3 4 5
1
4 2
2 1 4 3
1 3
4 2
4 3 2 1
1 3
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
# n = int(input())
# for m in range(n):
#     b = list(map(int,input().split()))
#     a = list(map(int,input().split()))
#     p = list(map(int,input().split()))
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])
#     a.sort()

#     for j in range(len(p)):
#         for i in range(len(p)):
#             if c[p[i]-1]>c[p[i]]:
#                 temp = c[p[i]-1]
#                 c[p[i]-1]=c[p[i]]
#                 c[p[i]]=temp
#     # print(c)
#     # print(a)
#     if c!=a:
#         print("NO")
#     elif c==a:
#         print("YES")

# a = [2,3,4,5]
# a = a.sort()
# print(a)





'''
None : 空
a = [2,3,4,5]
a = a.sort()
print(a)



串列.index(data)

大到小
a = [2,6,7,3,1]
a.sort(reverse = True)
b = sorted(a,reverse =  True)
print(b)

#數對排序
a = [[1,2],[1,4],[1,4,5],[1,4,4]]
a.sort()
print(a)


a = ['a','r','s','h']
a.sort()
print(a)

每一個文字，會用一個數字來代表他，ascii


如何獲得 字元 的 ascii
ord()
a = ['a','r','s','h']
a.sort()
for i in a:
    print(ord(i))

#判斷英文字母的方法
a = ord("a")
b = ord("z")

c = ord("A")
d = ord("Z")

string = input()
for i in string:
    if a <= ord(i) <= b or c <= ord(i) <= d:
        pass
    else:
        print(False)
        break
else:
    print(True)


盡量用內建的函式，


logn:
n = 4
logn = 2
n = 8 
logn = 3

logn < n
n*logn  < n*n


'''

<<<<<<< HEAD
# a = list(map(int,input().split()))
# b = []
# e = []
# ii =0
# jj =0
# g = False
# f = 0
# count = 10**9
# dire = [[-1,0],[1,0],[0,-1],[0,1]]
# for i in range(a[0]):
#     c = list(map(int,input().split()))
#     b.append(c)
# d = [[0]*a[1] for i in range(a[0])]
# for i in range(a[0]):
#     for j in range(a[1]):
#         if b[i][j]<count:
#             count = b[i][j]
#             x = i
#             y = j
# d[x][y]=1
# while True:
#     count = 10**9
#     for k in range(len(dire)):
#         now_i=x+dire[k][0]
#         now_j=y+dire[k][1]
#         if 0<=now_i<a[0] and 0<=now_j<a[1]:
#             if b[now_i][now_j]<count and d[now_i][now_j]!=1:
#                 g = True
#                 count = b[now_i][now_j]
#                 ii = now_i
#                 jj = now_j

#     if g==False:
#         break 

#     x = ii
#     y = jj   
#     d[x][y]=1
#     g = False
# for i in range(a[0]):
#     for j in range(a[1]):
#         if d[i][j]==1:
#             f+=b[i][j]
# print(f)














=======
>>>>>>> 1df8540940941433d8272d553797fba1d9976652
'''
回家作業
字母變大寫 字串.upper()
字母變小寫 字串.lower()


https://leetcode-cn.com/problems/rearrange-words-in-a-sentence/

「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text :

句子的首字母大写
text 中的每个单词都用单个空格分隔。
请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。

请同样按上述格式返回新的句子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rearrange-words-in-a-sentence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


text = "Leetcode is cool"
text = text.split()
text = text.lower()
text = "Leetcode is cool"
text = text.lower()
print(text)
'''
# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         text = text.lower()
#         text = text.split() 
#         for i in range(len(text)):
#             text[i] = [len(text[i]),i,text[i]]
#         text.sort()
#         ans = ""
#         print(text[0][1])
#         text[0][2] = text[0][2][0].upper() + text[0][2][1:]
#         for i in text[:-1]:
#             ans += i[2] + " "
#         ans += text[-1][2]
                
#         print(ans)
        
#         return ans
text = "Keep calm and code on"
text = list(text.split())
ans = ""
for j in range(len(text)):
    for i in range(len(text)-1):
        if len(text[i])>len(text[i+1]):
            temp = text[i]
            text[i]= text[i+1]
            text[i+1]=temp
for i in range(len(text)):
    if i==0:
        text[i]=text[i][0].upper()+text[i][1:]
    else:
        text[i]=text[i].lower()
    ans+=text[i]
    ans+=" "
print(ans)


'''

灌溉田地

'''
# n = int(input())
# count = 1
# b = list(map(int,input().split()))
# c = []
# for j in range(n):
#     for i in range(j-1,0,-1):
#         if i==j-1:
#             if b[j]>=b[i]:
#                 count+=1
#             else:
#                 break
#         else:
#             if b[i]>=b[i-1]:
#                 count+=1
#             else:
#                 break
#     for i in range(j+1,n-1):
#         if i == j+1:
#             if b[j]>=b[i]:
#                 count+=1
#             else:
#                 break
#         else:
#             if b[i]>=b[i+1]:
#                 count+=1
#             else:
#                 break
#     print(j,count)
#     c.append(count)
#     count = 0
# print(max(c))

# a = [[],1,2]
# a.remove([])
# print(a)


'''
第一單元 
符號不動冥王
'''
# letter = "abcdefghijklmnopqrstuvwxyz"


# string = list(input())
# i = 0
# j = len(string) - 1
# while i < j:
#     if string[i] in letter and string[j] in letter:
#         string[i],string[j] = string[j],string[i]
#         i += 1
#         j -= 1
#     else:
#         if string[i] not in letter:
#             i += 1
#         if string[j] not in letter:
#             j -= 1

# print("".join(string))

'''
https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

numbers = [2,7,11,15], target = 9
[1,2]

输入：numbers = [2,3,4], target = 6
输出：[1,3]


输入：numbers = [-1,0], target = -1
输出：[1,2]

 非递减數列
O(n)
'''

# numbers = [2,7,11,15]
# target = 9



'''
https://leetcode-cn.com/problems/merge-sorted-array/

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

nums1 = [1,3,5]
nums2 = [2,4]

O(n+m)
'''
# nums1 = [4, 5, 6, 10, 11, 13] 

# m = 3
# nums2 = [5, 9, 11, 13, 17, 19]
# n = 3
# left1=0
# left2=0
# #right1=len(num1)-1
# #right2=len(num2)-1
# new=[]
# while len(new)<len(nums1)+len(nums2):
#     print(left1,left2)
#     if nums1[left1]<=nums2[left2]:
#         if  left1 == len(nums1) - 1:
#             new.append(nums1[left1])
#             #加入後半部
#             new=new+nums2[left2:]
#             break   
#         new.append(nums1[left1])
#         left1+=1

#     else:
#         if  left2 == len(nums2) - 1:
#             new.append(nums2[left2])
#             #加入後半部
#             new=new+nums1[left1:]
#             break   
#         new.append(nums2[left2])
#         left2+=1

#     print(new)
# print(new)

'''

點石成金

'''

# a = list(map(int,input().split()))

# b = list(map(int,input().split()))

# n = int(input())

# total = 0

# for i in range(len(a)): #n
#     if b[i]:
#         total += a[i]
# # print(total)
# maxv = 0
# for i in range(len(a)-n+1): #n /2
#     temp = 0
#     for j in range(i,i+n):  #n/2
#         if b[j] == 0:
#             temp += a[j]
#     maxv = max(maxv,temp)
# print(total + maxv)





'''
前綴和

求出最小連續子數組之和


'''
# n,m = map(int,input().split())

# k = list(map(int,input().split()))

# pre = []
# pre.append(0)
# c = 0
# for i in range(n):
#     c += k[i]
#     pre.append(c)

# minv = 10**9
# ans = 0
# for i in range(n-m+1):
#     # print(i,i+m)
#     temp = pre[i+m] - pre[i]
#     if temp < minv:
#         minv = temp
#         ans = i
# print(ans+1)

'''
前綴和簡單應用

點石成金

'''
# a=input().split() #2 1 3 0 2 8 5
# a=list(map(int,a))
# b=input().split() #1 0 1 1 0 1 0
# b=list(map(int,b))
# c=int(input()) #強制成功範圍

# #前綴和
# pre = [0]
# count = 0
# ans = 0
# for i in range(len(a)):
#     if b[i] == 0:
#         count += a[i]
#     else:
#         ans += a[i]
#     pre.append(count)

# maxv = -10**9
# for i in range(len(a)-c+1):
#     temp = pre[i+c] - pre[i]
#     if temp > maxv:
#         maxv = temp
# print(ans+maxv)


'''
前綴和簡單應用

(用前綴合去做)
輸入 一串數列 
輸入 index
輸入 target (保證不會大於數列總和)

當前index的數字 + 之後到終點索引值之間的數字 總和滿足大於等於 target ， 輸出該索引值


輸出
索引值



ex 1
2 1 5 4 3 5 3
0
8 

2
ex2
2 1 5 4 3 5 3
4
9

6
ex2 
2 1 5 4 3 5 3
5
20

3
'''
# a = list(map(int,input().split()))
# index = int(input())
# target = int(input())

# pre = [0]
# sum = 0
# for i in a:
#     sum += i
#     pre.append(sum)

# target += pre[index]
# if target > pre[-1]:
#     target -= pre[-1]
#     index = 0

# for i in range(index,len(pre)):
#     if pre[i] >= target:
#         print(i-1)
#         break




'''
前綴和 進階練習
支點切割
https://zerojudge.tw/ShowProblem?problemid=f638
'''

'''
差分

情境:
輸入一個數列
輸入n
接下來有n行
每一行輸入 c s e
代表 +c s起點 e終點
輸出修改完的數列

'''
'''
差分
https://leetcode.cn/problems/car-pooling/submissions/

'''
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         dif = [0]*1001
#         for i in trips:
#             dif[i[1]] += i[0]
#             dif[i[2]] -= i[0]
#         pre = []
#         total = 0
#         for i in dif:
#             total += i
#             pre.append(total)
#         for i in pre:
#             if i > capacity:
#                 return False
#                 break
#         else:
#             return True 
'''
差分進階練習
https://zerojudge.tw/ShowProblem?problemid=g597
'''


'''
二分搜尋 進階練習

圓環出口
https://zerojudge.tw/ShowProblem?problemid=f581

7 3
2 1 5 4 3 5 3
8 2 1 5 
9 4 3 5
12 3 2 1 5 4

4

4 3
1 3 5 7
4 1 3
1 4 8 12
4 1

'''
# n,m = map(int,input().split())
# p = list(map(int,input().split()))
# t = list(map(int,input().split()))

# sum_pre = [0]
# c = 0
# for i in range(n):
#     c += p[i]
#     sum_pre.append(c)

# # print(sum_pre)
# now = 1
# for x in t:
#     target = x + sum_pre[now-1]

#     if target > sum_pre[-1]:
#         target -= sum_pre[-1]
#         now = 1
#     i = now
#     j = n
#     while i < j:
#         mid = (i+j) // 2
#         if sum_pre[mid] == target:
#             now = mid + 1
#             break
#         elif sum_pre[mid] > target:
#             j = mid 
#         else:
#             i = mid + 1
#     else:
#         now = j + 1
#     now = ((now-1)%n+1)
# print(now-1)