"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Create a hashSet of the nums list
    num_set = set(nums)

    if len(nums) == 0:
        return 0

    ret = 1

    for i in range(len(nums)):
        # First check if nums[i] is the first number in its sequence
        if nums[i] - 1 in num_set:
            continue
        else:
            size = 1
            value = nums[i]

            while value + 1 in num_set:
                size += 1

                if size > ret:
                    ret = size
                
                value += 1
    
    return ret

