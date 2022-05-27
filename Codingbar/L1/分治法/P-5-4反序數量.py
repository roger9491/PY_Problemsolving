from operator import le
from turtle import right


def dac(i,j):
    # print(i,j)
    global ans
    if i >= j:
        return
    else:
        mid = (i + j) // 2
        temp1 = sorted(a[i:mid+1])
        temp2 = sorted(a[mid+1:j+1])
        left = 0
        right = 0
        c = 0
        # print(temp1,temp2)
        while left < len(temp1) or right < len(temp2):
            
            if temp1[left] > temp2[right]:
                c += 1
                right += 1
                if right == len(temp2):
                    c += right*(len(temp1) - left - 1)
                    break
            else:
                left += 1
                if left == len(temp1):
                    break
                c += (right)
        #     print(left, right,"c",c)
        # print(c)
        ans += c 


        dac(i,mid)
        dac(mid+1,j)
        return            
n = int(input())
a = list(map(int,input().split()))
ans = 0
dac(0, n-1)
print(ans)



# ans_2 = 0
# for i in range(n):
#     for j in range(i+1,n):
#         if a[i] > a[j]:
#             ans_2 += 1
# print(ans_2)


#345 435 3354 | 12 32 123 934 

def sortr(l,r):
    global count
    left=len(l)-1
    right=len(r)-1
    TheList=[]
    while right>=0 and left>=0:
        if l[left]>r[right]:
            TheList=[l[left]]+TheList
            left-=1
            count+=(right+1)
            #print(count," ",l," ",r," ",left," ",right+1)
        elif l[left]<r[right]:
            TheList=[r[right]]+TheList
            right-=1
        else:
            TheList=[r[right]]+TheList
            right-=1
    #print(TheList)
    if right==-1:
        TheList=l[:left+1]+TheList
    elif left==-1:
        TheList=r[:right+1]+TheList
    #print(TheList)
    return TheList
def mergesort(lis):
    if len(lis)==1:
        return lis
    else:
        left=lis[:len(lis)//2]
        right=lis[len(lis)//2:]
        left=mergesort(left)
        right=mergesort(right)
        final=sortr(left,right)
        return final
    
#stack
x=input()
count=0
inf=list(map(int,input().split()))

mergesort(inf)
print(count)