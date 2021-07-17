t = int(input())

for i in range(t):
    e = input()
    x1, y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())

    if (x1 == x2 and x2 == x3 and min(y1,y2) < y3< max(y1,y2) or (y1 == y2 and y2 == y3 and min(x1,x2) < x3< max(x1,x2))) :
        print(abs(x1-x2)+abs(y1-y2) + 2)
    else:
    
        print(abs(x1-x2)+abs(y1-y2))
   