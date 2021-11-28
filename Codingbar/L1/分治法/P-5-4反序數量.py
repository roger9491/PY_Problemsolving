def dac(i,j):
    global ans
    if i >= j:
        return
    else:
        mid = (i + j) // 2
        temp1 = sorted(a[i:mid+1])
        temp2 = sorted(a[mid+1:j+1])
        right = 0
        left = 0
        count = 0
        flag = False
        print(i,j,count)
        print(temp1,temp2)
        print(left,right,ans,count)
        while left <= (mid-i):
            
            if temp1[left] <= temp2[right]:
                left += 1
                if flag:
                    ans += count
                    flag = False
            else:
                flag = True
                count += 1
                if right < j - (mid+1):
                    right += 1
                else:
                    if flag:
                        ans += count
                        flag = False
                    left += 1
            print(left,right,ans,count)
        if flag:
            ans += count
        print
        dac(i,mid)
        dac(mid+1,j)
        return            
n = int(input())
a = list(map(int,input().split()))
ans = 0
dac(0, n-1)
print(ans)



ans_2 = 0
for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            ans_2 += 1
print(ans_2)


# 435 345 3354 | 12 32 123 934 