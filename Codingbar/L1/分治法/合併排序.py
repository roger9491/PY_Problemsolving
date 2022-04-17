
def mergesort(i, j):
    if i == j:
        return i
    else:
        mid = (i + j) // 2
        mergesort(i, mid)
        mergesort(mid+1,j)
    # print(i,j)
    temp = []
    mid = (i + j) // 2
    s = i
    e = j
    j = mid + 1
    while i <= mid or j <= e:
        # print(i,j)
        if (j > e or nums[i] <= nums[j]) and i <= mid:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1

    # print(temp)
    # print(nums)
    # print(i,j)
    nums[s:e+1] = temp
    # print(nums)
    return nums

nums = [1,454,234,12,6,234,321456,65412,342]
print(mergesort(0, len(nums)-1))