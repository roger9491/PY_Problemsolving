def max_sub_array(i,j,nums):
    if i == j:
        return nums[i]
    else:
        mid = (i + j) // 2 
        max_left  = max_sub_array(i,mid,nums)
        max_right = max_sub_array(mid+1, j,nums)
    print(i,j)
    #合併
    if j - i == 1:
        maxr = nums[j]
        maxl = nums[i]
    else:
        maxl = nums[(i+j)//2]
        temp = 0
        for x in range((i+j)//2 , i-1, -1):
            temp += nums[x]
            maxl = max(maxl,temp)

        maxr = nums[(i+j)//2+1]
        temp = 0
        for x in range((i+j)//2+1, j+1):
            temp += nums[x]
            maxr = max(maxr,temp)
    print(max_left, max_right, maxl, maxr)
    return max(max_left, max_right, maxr+maxl)
    # n = len(nums)
    #     #递归终止条件
    # if n == 1:
    #     return nums[0]
    # else:
    #     #递归计算左半边最大子序和
    #     max_left = max_sub_array(0,0,nums[0:len(nums) // 2])
    #     #递归计算右半边最大子序和
    #     max_right = max_sub_array(0,0,nums[len(nums) // 2:len(nums)])
    # print(nums)
    # #计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
    # max_l = nums[len(nums) // 2 - 1]
    # tmp = 0
    # for i in range(len(nums) // 2 - 1, -1, -1):
    #     tmp += nums[i]
    #     max_l = max(tmp, max_l)
    # max_r = nums[len(nums) // 2]
    # tmp = 0
    # for i in range(len(nums) // 2, len(nums)):
    #     tmp += nums[i]
    #     max_r = max(tmp, max_r)
    # print(max_right,max_left,max_l,max_r)
    # #返回三个中的最大值
    # return max(max_right,max_left,max_l+max_r)






nums = list(map(int,input().split()))
nums = [1,2,-1,-2,2,1,-2,1]
print(max_sub_array(0, len(nums)-1, nums))