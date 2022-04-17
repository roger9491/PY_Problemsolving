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