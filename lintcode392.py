"""
最大不相邻子序列和
lintcode: 392.打劫房屋
"""


# 递归 27%时超出时间限制
def max_sum(nums):

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0], nums[1])

    if len(nums) == 3:
        return max(nums[0]+nums[2], nums[1])

    return max(nums[0]+max_sum(nums[2:]), nums[1]+max_sum(nums[3:]))


# 递归转for循环  O(n)时间复杂度、O(n)空间复杂度
def max_sum2(nums):

    if not nums:
        return 0

    res = [-1] * len(nums)

    for i in range(len(nums)):
        if i < 2:
            res[i] = nums[i]
        elif i == 2:
            res[i] = max(nums[1], nums[0]+nums[2])
        else:
            res[i] = max(nums[i]+res[i-2], res[i-1])
            # res[i] = max(nums[i]+res[i-2], nums[i]+res[i-3])

    return max(res)


# O(n)时间复杂度、O(1)空间复杂度
def max_sum3(nums):

    if not nums:
        return 0

    res = [-1] * 3

    for i in range(len(nums)):
        if i < 2:
            res[i] = nums[i]
        elif i == 2:
            res[2] = max(nums[1], nums[0]+nums[2])
        else:
            res[i % 3] = max(nums[i]+res[(i-2) % 3], res[(i-1) % 3])

    return max(res)


if __name__ == '__main__':
    nums = [1, 5, 3, 4, 1, 7, 1, 8]

    print(max_sum(nums))
    print(max_sum2(nums))
    print(max_sum3(nums))
