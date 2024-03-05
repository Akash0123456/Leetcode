"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ret = []
    pre = 1
    # Iterate through nums and get the product of all the values before i
    for i in range(len(nums)):
        if i is 0:
            ret.append(pre)
        else:
            pre = pre * nums[i-1]
            ret.append(pre)

    post = 1
    # Iterate through nums backwards and get the product of all the values after i
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums) - 1:
            continue
        else:
            post = post * nums[i+1]
            ret[i] = ret[i] * post
    
    return ret