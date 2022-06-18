# t = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# t[0][]
# t[1][2]
# a = [0,0,0] #一維
# a[0]

# t = [[5,4,10,2],[1,4,8,1],[9,8,0,9]]
# n,m = map(int,input().split())
# matrix = []
# for i in range(n):
#     a = list(map(int,input().split()))
#     matrix.append(a)
# print(matrix)
# print(matrix[1][2])
# t = list(map(int,input().split()))
# print(n,m)
# print(t[0],t[1])


'''
a = list(map(int,input().split()))
yee = -10000
for i in range(len(a)):
    if yee < a[i]:
        yee = a[i]
print(yee)
'''
n = int(input())
for i in range(n):
    a = input()
    a = a.split()
    a = list(map(int,a))

    bee = []
    yee = 0

    # for k in range(len(a)):
    #     for h in range(k+1,len(a)):
    #         if a[k] >= a[h]:
    #             yee = a[k] - a[h]
    #         elif a[k] < a[h]:
    #             yee = a[h] - a[k]
    #         bee.append(yee)
    a.sort()    #O(nlogn)
    # for i in range()  找出前後最短O(n)
    print(min(bee))

'''

N*
O((3*N**2-N)/2) =>O(N**2)
n**2 = > 100
nlogn => 10*(3~4)
logn => 2的幾次方==n
log10 => 2的幾次方==10
log10 => 3 ~ 4

2的幾次方==10**5    100000

2**10 => 1024 => 10**3 * 10**3
2**20

oj => 10**6 ~ 10**7

10**3

10**5 O(n**2) n*n => 10**5 * 10**5
        O(nlog n) =>10**5 log 10**5   => 10**5 * 20 => 2 * 10**6
        求log10**5 因為 2**20 > 10**5
                    log10**6 > log10**5
                    20    > log10**5
        10**5 * 20 > 10**5 log10**5  
        10**5 * 20  符合 10**6 ~ 10**7

核心想法 小的很難算  大的數字很好算
      若是 大的數字符合題目規定
      小的 也一定符合
         

'''

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
# text = "Keep calm and code on"
# text = list(text.split())
# ans = ""
# for j in range(len(text)):
#     for i in range(len(text)-1):
#         if len(text[i])>len(text[i+1]):
#             temp = text[i]
#             text[i]= text[i+1]
#             text[i+1]=temp
# for i in range(len(text)):
#     if i==0:
#         text[i]=text[i][0].upper()+text[i][1:]
#     else:
#         text[i]=text[i].lower()
#     ans+=text[i]
#     ans+=" "
# print(ans)


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

# g = list(map(int,input().split()))
# magic = list(map(int,input().split()))
# Range = int(input())
# old_total = 0
# for i in range(len(magic)):
#     if magic[i] == 1:
#         old_total = old_total + g[i]
# All = []
# # 時間複雜度太高了
# for i in range(len(g)-Range+1):
#     plus = 0
#     for k in range(Range):  #區間和 O(range) => O(1)
#         if magic[i+k] == 0:
#             plus = plus + g[k+i]
#     All.append(plus)

# final_plus = max(All)
# print(old_total + final_plus)

'''
輸入 一個數列
輸入 一個數字區間大小



輸出 最小區間和

ex
(1)
2 1 3 0 2 8 5
3


4
利用前綴和
'''



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


