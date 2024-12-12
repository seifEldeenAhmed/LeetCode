def findMin(nums) :
    target = 0
    l = 0
    r = len(nums) - 1
    while l < r:
        target = l+(r-l) // 2
        if nums[target] > nums[r]:
            l = target+1
        else:
            r = target
    return nums[l]


print(findMin([6,7,8,1,2,3,4,5]))