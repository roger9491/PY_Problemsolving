# def  f(n):
#     print(n)
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return f(n-1) + f(n-2)

'''
定義 函式:f(n): 1+~+n
f(98)  = f(97) + 98
f(99)  = f(98) + 99
f(100) = f(99) + 100

f(1) = 1    初始值 邊界
f(n) = f(n-1) + n   遞迴關係式
原本的問題 = 較小的問題 + c

return 函式回傳
'''

# print(f(6))

'''
快速排序法
1 7 9 10 2 8 15


小到大
基準點  1 
i = 1
j = 2
1 7 9 10 2 8 15 
特殊條件



版本
8 7 9 10 2 8 15
基準點  8   0
i = 2   比基準點大的
j = 4   比基準點小的
8 7 2 10 9 8 15

i = 3
j = 3
if 基準點 < 碰面
    i = i - 1
基準點 跟 i 互換

做到 i 與 j 碰面






分
基準點
...小....基準點...大...
1.  ...小....
    小    基準點   大
    2.    小 
        小    基準點   大
合併
...小.... 排完之後
...大... 排完之後




...小....基準點...大...
小到大
'''

def quicksort(i, j):
    if i >= j:
        return
    else:   #分
        print(i,j)
        print("befor",nums)
        left = i    #原本
        right = j

        pivot = i   #基準點
        i += 1
        while i < j:    #小 .. 基準點 .. 大
            if nums[i] > nums[pivot] and nums[j] < nums[pivot]:
               nums[i], nums[j] = nums[j], nums[i]     
            else:
                if nums[i] <= nums[pivot]:
                    i += 1
                if nums[j] >= nums[pivot]:
                    j -= 1
        if nums[pivot] < nums[i]:
            i -= 1
        nums[pivot], nums[i] = nums[i], nums[pivot]
        print("after",nums)
        pivot = i
        # ...小...基準點...大...
        # ...小... 若排好 ...大... 若排好
        # 跟基準點 合併 排好...小...基準點...大...
        quicksort(left, pivot - 1)
        quicksort(pivot + 1, right)  #大
        return nums
            
nums = list(map(int,input().split()))
print(quicksort(0, len(nums)-1))


'''
剩三個
5 1 9   0 2
p = 5
i = 1
1 5 9

剩二個
9 1
p = 9
i = j
1 9

'''

