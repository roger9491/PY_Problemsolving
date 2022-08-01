'''

while

    找切點


7 3
2 4 1 3 7 6 9

m 4 1 3 7 6 

4
'''
# a = [2 ,4, 1, 3, 7, 6, 9]

# sum1 = [0]
# c1 = 0
# sum2 = [0]
# c2 = 0
# for i in range(len(a)):
#     c1 += a[i]
#     sum1.append(c1)
#     c2 += a[i]*(i+1)
#     sum2.append(c2)

# for i in range(1,6):    #迭帶m的可能姓
#     m = a[i]
#     temp = sum2[-1] - sum1[-1]*m
#     print(i,abs(temp))   




# for i in range(1,6):    #迭帶m的可能姓
#     m = a[i]
#     temp = 0
#     for j in range(1,len(a)+1):
#         c = (a[j-1]*(j-m))
#         temp += c
#     print(i,abs(temp))
# a = [2 ,4, 1, 3, 7, 6, 9]
#     #切一個層級 切割的終止條件有兩個：子陣列範圍小於3或切到給定的層級K就不再切割。而
#     [[2],[1,3,7,6,9]]
#     #切二層
#     [[2],[1,3],[6,9]]   #終止
# for i in range(3,6):    #迭帶m的可能姓
#     m = a[i]
#     temp = 0
#     #O(1)
#     # for j in range(2,len(a)):   #固定m算總和
#     #     temp += (a[j]*(j-m))
#     print(m,abs(temp))

'''
0 ~ 8 
i : 0 ~ 3

p[0]*(0-m) + p[1]*(1-m) + p[2]*(2-m) + p[3]*(3-m)
(p[0]*0-p[0]*m) + (p[1]*1-p[1]*m) + (p[2]*2-p[2]*m) +　(p[3]*3-p[3]*m)
(p[0]*0 +p[1]*1 + p[2]*2 + p[3]*3) - (p[0]*m + p[1]*m + p[2]*m + p[3]*m)
(p[0]*0 +p[1]*1 + p[2]*2 + p[3]*3) - (p[0]+ p[1] + p[2] + p[3])*m
              O(1)                          O(1) => O(1)
(p[0]*0 +p[1]*1 + p[2]*2 + p[3]*3) 前綴和

[p[0]*0, p[0]*0 +p[1]*1, p[0]*0 +p[1]*1 + p[2]*2, p[0]*0 +p[1]*1 + p[2]*2 + p[3]*3]

'''


'''

二分搜尋    條件: 串列必須是 小~大 大到小   O(logn)
            猜的數字一律固定在 下 ~ 上 的中間
下  上      log 統一都是2為底
0 ~ 100     n   每一次猜完都會使
#50             範圍變 一半
51 ~ 100    log8 = 3
#75
50 ~ 75
#63     62
63 ~ 75
#69     69
70 ~ 75
#73     72
70 ~ 72
#72     71  猜中
70 ~ 71
#70
71 ~ 71 
71

'''
# a = []
# for i in range(101):
#     a.append(i)
# print(a)

# target = int(input())
# i = 0   #下界
# j = 100 #上界

# while i <= j: 
#     mid = (i+j) // 2
#     print(i,j)
#     if a[mid] == target:
#         print(mid)
#         break
#     elif a[mid] > target:
#         j = mid - 1
#     else:
#         i = mid + 1
'''
建立一個串列 串列大小為 20~40
隨機加入數字(1,40) 湊滿這個大小

排序

輸入一個數字 

去搜尋這個數字 存在 印出 索引值
            不存在 印出 不存在

'''
# import random

# length = random.randint(20,40)
# print(length)
# a = []

# while len(a) < length:
#     n = random.randint(1,60)
#     if n not in a:
#         a.append(n)
# a.sort()
# print(a)

# target = int(input())
# i = 0   #下界
# j = length - 1 #上界

# while i <= j: 
#     mid = (i+j) // 2
#     if a[mid] == target:
#         print(mid)
#         break
#     elif a[mid] > target:
#         j = mid - 1
#     else:
#         i = mid + 1
# else:
#     print("不存在")


# def permutations(Str,index):
#     final=[]
#     final1=''
#     final2=''
#     #print(index)
#     #print(Str)
#     if Str[index]=='0':
#         final1=final1+'1'
#     else:
#         final1=final1+str(int(Str[index])-1)# 這裡加成-1 因為會是0
#     final2=final2+str(int(Str[index])+1)
#     for i in range(len(Str)-(index+1)):
#         final1=final1+'9'
#         final2=final2+'1'
#     final.append(final1)
#     #print(final1)
#     final.append(final2)
#     #print(final2)
#     return final
# import random
# while 1:
#     try:
#         # x=str(random.randint(1,999999))
#         x = "6"
#         ans=[]
#         now1=''
#         now2=''
#         o=''
#         l=''
#         for k in range(len(x)+1):
#             o=o+'1'
#         for m in range(len(x)-1):
#             l=l+'9'
#         for i in range(len(x)):
#             if int(x[i])%2==0:
#                 v=permutations(x,i) #會有4個ans
#                 now1=now1+v[0]
#                 now2=now2+v[1]
#                 break
#             else:
#                 now1=now1+x[i]
#                 now2=now2+x[i]
#         x=int(x)
#         now1=int(now1)
#         now2=int(now2)
#         o=int(o)
#         l=int(l)
#         #print(now1,now2,o,l,sep=' ')
#         ans.append(abs(x-now1))
#         ans.append(abs(x-now2))
#         ans.append(abs(x-o))
#         ans.append(abs(x-l))
#         #print(ans)
#         print(min(ans))
        
#     except:
#         print(x)
#         print("-9999999")
#         break

# while True:
#     try:
#         n=int(input())
#         temp_n = n
#         a = n
#         n = str(n)
#         n = list(n)
#         temp = []
#         temp = n.copy()
#         flag = False
#         for i in range(len(n)):
#             if int(n[i])%2==0:
#                 flag = True
#         if flag == False:
#             print(0)
#         elif flag == True:
#             flag = False
#             for i in range(len(n)):
#                 if flag == False:
#                     if int(n[i])%2==0:
#                         n[i]=int(n[i])+1
#                         flag = True
#                 elif flag == True:
#                     n[i]=1
#             flag = False
#             for i in range(len(temp)):
#                 if flag == False:
#                     if int(temp[i])%2==0:
#                         if int(temp[i])==0:
#                             temp[i]=9
#                             if i!= 0:
#                                 if temp[i-1]=='1':
#                                     temp[i-1]='0'
#                                 else:
#                                     temp[i-1]=int(temp[i-1])-2
#                         else:
#                             temp[i]=int(temp[i])-1
#                         flag = True
#                 elif flag == True:
#                     temp[i]=9
#             n = list(map(str,n))
#             temp = list(map(str,temp))
#             n = "".join(n)
#             temp = "".join(temp)
#             if a-int(temp) == 2:
#                 print(temp_n)
#             else:
#                 if (int(n)-a)>(a-int(temp)):
#                     print(a-int(temp))
#                 else:
#                     print(int(n)-a)
#     except:
#         break



'''
set() : 集合 不會有重複資料

建立 
s = set()

加入
s.add()

刪除
s.remove()

交集
a = set()
b = set()
c = a & b

聯集
a = set()
b = set()
c = a | b

'''
# l = [1,"2","1","1",2,3]

# l2 = [1,2,3]
# l3 = l & l2

# print(l3)

# s = {}
# print(type(s))

'''

字典


dic = {鍵值:值}

如何取值?
    跟串列幾乎一樣
    鍵值取值
    <鍵值必須唯一>
    時間複雜度 O(1)
    為什麼?


'''
# dic = {"謝詠宸":153, "莊心睿":175 ,"李博凱":180,"謝詠宸":165 }
# print(dic["謝詠宸"])


# a = list(map(int,input().split()))
# b = []
# right = [6,2,1,5]
# forward = [4,1,3,6]
# for i in range(a[0]):
#     b.append(1)
# for i in range(a[1]):
#     c = list(map(int,input().split()))
#     if c[1]==-1:
#         for j in range(len(forward)):
#             if b[c[0]-1]==forward[j]:
#                 if j==3:
#                     b[c[0]-1]=forward[0]
#                     break
#                 else:
#                     b[c[0]-1]=forward[j+1]
#                     break
#             elif b[c[0]-1]==5:
#                 b[c[0]-1]=3
#                 break
#             elif b[c[0]-1]==2:
#                 b[c[0]-1]=4
#                 break
#     elif c[1]==-2:
#         for j in range(len(right)):
#             if b[c[0]-1]==right[j]:
#                 if j==3:
#                     b[c[0]-1]=right[0]
#                 else:
#                     b[c[0]-1]=right[j+1]
#                 break
#             elif b[c[0]-1]==3:
#                 b[c[0]-1]=6
#                 break
#             elif b[c[0]-1]==4:
#                 b[c[0]-1]=1
#                 break
#     elif c[0]>0 and c[1]>0:
#         temp = b[c[0]-1]
#         b[c[0]-1]=b[c[1]-1]
#         b[c[1]-1]=temp
# b = list(map(str,b))
# print(" ".join(b))

def cut(s,t,k):
  global p
  if t-s < 3 or k < 1:
    return 0
  move = s + 1
  left = pre[s]
  right = 0
  for i in range(s+2,t):
    right += p[i] * (i-s-1)

  dif = abs(right - left)
  while move < t - 1:
    left = left + pre[move]
    move += 1
    right = right - backsum[move]
    #backsum[move] = backsum[move+1]
    dif_2 = abs(right - left)
    if dif_2 >= dif:
      break
    dif = dif_2
  move -= 1
  return p[move] + cut(s, move, k-1) + cut(move+1, t, k-1)
    
# main 
n, k = map(int,input().split())
p = [int(x) for x in input().split()]
#p = list(map(int, input().split()))
# [2, 4, 1, 3, 7, 6, 9]
#print(p)
psum = 0
pre = []
for i in range(len(p)):
  psum += p[i]
  pre.append(psum)
bsum = 0
backsum = []
for i in range(len(p)-1,-1,-1):
  bsum += p[i]
  backsum.append(bsum)
backsum = backsum[::-1]
#print(pre)
#[2, 6, 7, 10, 17, 23, 32]
#print(back)
#[32, 30, 26, 25, 22, 15, 9]

# 0    1    2    3    4    5    6
# 2    6    7    10   17   23   32 pre
# 32   30   26   25   22   15    9 back
print(cut(0,n,k))