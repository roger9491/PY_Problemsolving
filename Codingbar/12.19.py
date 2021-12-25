'''
二維矩陣練習

week2 邊緣偵測

'''
# def check(i,j):
#     dire = [[1,0],[0,1],[-1,0],[0,-1]]
#     for x in dire:
#         if g[x[0]+i][x[1]+j] == '0':
#             return False
#     return True



# n1 = int(input())
# n2 = int(input())

# g = []
# for i in range(n1):
#     s = input().split()
#     g.append(s)

# ans = [[0]*n2 for i in range(n1)]

# for i in range(n1):
#     for j in range(n2):
#         if g[i][j] == "0":
#             ans[i][j] = "_"
#         elif g[i][j] == "1":
#             if check(i,j):
#                 ans[i][j] = "_"
#             else:
#                 ans[i][j] = "0"
            
# for i in range(n1):
#     print(" ".join(ans[i]))
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

最大消波塊


'''

# a = list(map(int,input().split()))

# i = 0
# j = len(a) - 1
# ans = 0
# while i < j:

#     if ans < (j - i) * min(a[i],a[j]):
#         ans = (j - i) * min(a[i],a[j])
    
#     if a[i] > a[j]:
#         j -= 1
#     elif a[i] < a[j]:
#         i += 1
#     else:
#         i += 1
#         j -= 1
# print(ans)



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

























