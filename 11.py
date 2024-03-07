"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1
"""

def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    ret = 0
    l = 0
    r = len(height) - 1

    while l < r:
        area = (r-l) * min(height[r], height[l])

        if height[r] > height[l]:
            l += 1
        elif height[r] <= height[l]:
            r -= 1
        
        if ret < area:
            ret = area
    
    return ret