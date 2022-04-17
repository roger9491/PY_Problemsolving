import random


def dac(i,j):
    print(i,j)
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
        print(temp1,temp2)
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
            # print(left, right,"c",c)
        # print(c)
        ans += c 


        dac(i,mid)
        dac(mid+1,j)
        return            



while True:
    n = 6
    a = []
    for i in range(6):
        a.append(random.randint(1,200))

    ans = 0
    dac(0, n-1)
    ans1 = ans
    ans2 = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                ans2 += 1

    if ans1 != ans2:
        print(6)
        print(" ".join(list(map(str,a))))
        break