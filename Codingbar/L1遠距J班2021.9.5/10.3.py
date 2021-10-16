'''
輸入 字串
輸入 首相
輸入 末向
輸入 間隔

印出 範圍裡的字串

入力文字列
首相に入る
入力端
入力間隔

範囲内の文字列を出力します
string[::] 不能用

ex
apple
0
4
1
appl

'''
# s = input()
# a = int(input())
# b = int(input())
# c = int(input())

# s1 = ""
# for i in range(a,b,c):
#     s1 += s[i]
# print(s1)

s = "apple"



'''
重複輸入數字 直到輸入no 結束
印出大值

ex
1
7
8
3
10
no

178310
ans = -10**9 (最大值)
a = [1,7,8,3,10] 串列


'''

# a = []
# while True:
#     s = input()
#     if s == "no":
#         break
    
#     a.append(int(s))
# print(a)

# maxv = -10**9
# for i in range(len(a)): #0~4
#     if maxv < a[i]:
#         maxv = a[i]
# print(maxv)





# numlist=[]
# stay=0
# while True:
#     x=input()
#     if x=='no':
#         break
#     numlist.append(x)
# numlist=list(map(int,numlist))
# numlist.append(0)
# for i in range(len(numlist)-1):
#     if numlist[i]>numlist[i+1]:
#         if numlist[i]>stay:
#             stay=numlist[i]
# print(stay)


'''
輸入一字串  (作業)
輸出 字串裡的數字

ex
a14gh7sdf9

14
7
9



'''

# sentence=input()
# sentence+='a'
# number=['1','2','3','4','5','6','7','8','9','0']
# strsumnum=''
# for i in sentence:
#     if i in number:
#         strsumnum+=i
#     else:
#         if len(strsumnum)!=0:
#             print(strsumnum)
#             strsumnum=''



'''
輸入 一列數字
印出 數之兩兩間 比較的結果

印出
print(a[i],>,a[i+1])
print(a[i],<,a[i+1])


1 2 4 61 12

1 < 2
2 < 4
4 < 61
61 > 12



'''
'''
1 8 9 19 3

'''


'''
實作join
'''

'''
實作replace (作業)
'''


'''
字條
輸入一串字串
印出字串的第一個字 一行一行印

'''

'''
輸入數字 判斷輸入的數字有沒有 "4"
有印出 1
沒     0

'''









'''
久富理右

重複輸入 輸入到no 程式結束

ex
5
6
no

'''


'''
重複輸入 把輸入的轉換成串列 並印出來 ，輸入到'no' 程式結束

ex
in
5 7 8 1
3 4 7 3
no
out
['5','7','8','1']
['3','4','7','3']
'''

'''
輸入一個整數ｎ，輸出 0 ~ n 一行一行輸出

in
7
out
0
1
2
3
4
5
6
7

'''

'''
建立一個串列 把串列裡的東西給印出來
'''

'''
輸入整數 判斷是否是質數
for 配 else
'''

'''
輸入整數 判斷是否是質數
不能用 for 配 else
'''

# n = 2 
# m = 4

# t = [[0]*m for i in range(n)]


# s = ""
# for i in range(5):
#     s += str(i)
# print("01234")
# a = [0,1,2,3,4]
# for i in range(5): #0~4
#     s *= a[i]
# print()


'''
(1) 魔王走到正確位址 同時下炸彈 串列
指定 五回合

'''

n,m,k = map(int,input().split())

now = []    #代表魔王的位置
move = []   #每一個魔王移動
matrix = [[0]*m for i in range(n)]  #matrix
for i in range(k):
    r,c,s,t = map(int,input().split())
    now.append([r,c])
    move.append([s,t])
print(now)
print(move)

#炸彈怎麼下
matrix[now[0][0]][now[0][1]] += 1

#移動
now[0][0] += move[0][0]
now[0][1] += move[0][1]

print(now) 
print(move)


'''
1 6 3
0 0 0 0
0 2 0 -1
0 4 0 2

4
'''