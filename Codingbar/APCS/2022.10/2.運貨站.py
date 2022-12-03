'''
運貨站
https://zerojudge.tw/ShowProblem?problemid=j123
'''

g = {'A': [[4,1],]}

r, c, n = map(int,input().split())

matrix = [[0]*c for i in range(r)]
start = [0]*r

for i in range(n):
    t, y = input().split()
    y = int(y)

    if t == "A":

