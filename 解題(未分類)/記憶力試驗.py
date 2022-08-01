'''
https://zerojudge.tw/ShowProblem?problemid=c631
'''
import sys
n = int(input())

string = ""
c = 0
while True:
    for line in sys.stdin.readline(1):
        c += 1
        string += line
        # print(line)
    # print(c)
    if c >= n:
        break
while True:
    try:
        l, r = map(int,input().split())
        print(string[l-1:r])
    except:
        break




