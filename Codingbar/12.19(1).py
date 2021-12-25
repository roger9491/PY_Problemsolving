# while True:
#     try:
#         r, c, m = map(int, input().strip().split())
#         templst = []
#         for i in range(r):
#             templst.append(list(map(int, input().split())))
#         lst = list(map(int, input().split()))
#         for i in lst[::-1]:
#             if i == 1:
#                 templst.reverse()
#             else:    
#                 anslst = []
#                 for i in range(c-1, -1, -1):
#                     anslst.append([])
#                     for j in range(r):
#                         anslst[-1].append(templst[j][i])
#                 c, r = r, c
#                 templst = anslst
                 
#         print(r, c)
#         for i in range(r):
#             for j in range(c):
#                 print(templst[i][j], end = '')
#                 if j != c-1:
#                     print(' ', end = '')
#             if i != r-1:
#                 print()
#         print()
#     except:
#         break

# while True:
#     try:
#         a=input()
#         a=a.split()
#         a=list(map(int,a))
#         R=a[0]
#         C=a[1]
#         M=a[2]
#         b=[]
#         c=[]
#         h=[]
#         f=[]
#         for i in range(R):
#             d=input()
#             d=d.split()
#             c.append(d)
#         e=input()
#         e=e.split()
#         e=e[::-1]
#         e=list(map(int,e))
#         for i in range(len(e)):
#             if e[i]==0:
#                 f = []
#                 for i in range(len(c[0])):     
#                     for j in range(len(c)):
#                         b.append(c[j][-(i+1)]) 
#                     f.append(b)
#                     b=[]
#                 c=f
#             elif e[i]==1:
#                 c=c[::-1]
#         print(len(c),len(c[0]))
#         for i in range(len(c)):
#             print(" ".join(list(map(str,c[i]))))
#     except:
#         break
# while True:
#     try:
#         a = list(map(int,input().split()))

#         c = []
#         for i in range(a[0]):

#             b = list(map(int,input().split()))
#             c.append(b)
#         d = list(map(int,input().split()))
#         for i in range(len(d)-1,-1,-1):
#             e = []
#             f = []
#             g = []
#             if d[i]==0:
#                 for l in range(3):
#                     for j in range(len(c[0])):
#                         for k in range(len(c)-1,-1,-1):
#                             e.append(c[k][j])
#                         f.append(e)
#                         e = []
#                     c = f
#                     f = []
#             elif d[i]==1:
#                 for j in range(len(c)-1,-1,-1):
#                     g.append(c[j])
#                 c = g
#         print(len(c),len(c[0]))

#         for i in range(len(c)):
#             print(" ".join(list(map(str,c[i]))))
#     except:
#         break

# while True:
#     try:
#         a = list(map(int,input().split()))
#         c = []
#         e = []
#         f = []
#         g = []

#         for i in range(a[0]):
#             b = list(map(int,input().split()))
#             c.append(b)

#         d = list(map(int,input().split()))
#         for i in range(len(d)-1,-1,-1):
#             e = []
#             f = []
#             g = []
#             if d[i]==0:
#                 for l in range(3):
#                     for j in range(len(c[0])):
#                         for k in range(len(c)-1,-1,-1):
#                             e.append(c[k][j])
#                         f.append(e)
#                         e = []
#                     c = f
#                     f = []
#             elif d[i]==1:
#                 for j in range(len(c)-1,-1,-1):
#                     g.append(c[j])
#                 c = g
#         print(len(c),len(c[0]))

#         for i in range(len(c)):
#             print(" ".join(list(map(str,c[i]))))
#     except:
#         break
'''

3 3

2 13 4
3 11 5
1 20 7

'''