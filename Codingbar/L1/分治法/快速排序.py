def quicksort(i, j):
    if i >= j:
        return 
    else:
        print("pivot",i)
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
