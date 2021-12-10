def quicksort(i, j):
    if i >= j:
        return 
    else:
        left = i
        right = j
        print(left,right)
        
        pivot = i
        print("pivot",pivot)
        i += 1
        while i < j:
            if nums[i] > nums[pivot] and nums[j] < nums[pivot]: 
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] <= nums[pivot]:
                i += 1
            if nums[j] >= nums[pivot]:
                j -= 1
        if nums[i] > nums[pivot]:
            i -= 1
        nums[i], nums[pivot] = nums[pivot], nums[i]
        pivot = i 
    print(nums)
    quicksort(left, pivot-1)
    quicksort(pivot+1, right)
    return nums



nums = [1,454,234,12,6,234,321456,65412,342]
print(quicksort(0, len(nums)-1))


# def quick_sort(nums):
#     n = len(nums)

#     def quick(left, right):
#         if left >= right:
#             return nums
#         pivot = left
#         i = left
#         j = right
#         while i < j:
#             while i < j and nums[j] > nums[pivot]:
#                 j -= 1
#             while i < j and nums[i] <= nums[pivot]:
#                 i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#         nums[pivot], nums[j] = nums[j], nums[pivot]
#         quick(left, j - 1)
#         quick(j + 1, right)
#         return nums

#     return quick(0, n - 1)

'''
left = , right =  , pivot = 

left = 0, right = 6 , pivot = 6
+34 +98 +25 +83 +57 +74 +16 (1)
i = 34
j = 34
left = 1, right = 6 , pivot = 6
+16 +98 +25 +83 +57 +74 +34 (2)
i = 98
j = 25
+16 +25 +98 +83 +57 +74 +34
+16 +25 +34 +83 +57 +74 +98 (3)
left = 1, right = 2 , pivot = 2
+16 +25 +34 +83 +57 +74 +98 (4)

left = 3, right =  6, pivot = 6
+16 +25 +34 +83 +57 +74 +98 
+16 +25 +34 +83 +57 +74 +98 (5)

left = 3, right = 5 , pivot = 5 
+16 +25 +34 +83 +57 +74 +98
i = 83
j = 57
+16 +25 +34 +57 +83 +74 +98
+16 +25 +34 +57 +74 +83 +98 (6)

left = 3, right = 4 , pivot = 4 (7)

left = 4, right = 5 , pivot = 5 (8)

'''