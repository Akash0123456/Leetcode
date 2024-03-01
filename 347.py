from collections import defaultdict

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # Create a list that stores a list of the nums.
    # The index of the particular element is the freq of the number in nums
    
    # Create a dict to map the number ot its frequency {num: freq}
    freq_map = defaultdict(int)

    # Iterate through the list nums and populate freq_map
    for num in nums:
        freq_map[num] += 1
    
    """
    freq_map = 
    {
        1 : 3,
        2 : 2,
        3 : 1
    }
    """

    # Create the list that stores the list of nums by freq.
    freq_list = [[] for i in range(len(nums))]

    """
        freq_list = [[], [], []]
    """

    # Iterate through the dictionary and populate the list of lists by freq
    for num, freq in freq_map.items():
        x = freq - 1
        y = freq_list[x]
        freq_list[x].append(num)

    """
        [[3], [2], [1]]
    """
    
    # Get the k largest elements
    i = len(freq_list) - 1 
    j = 1

    res = []

    while i >= 0 and j <= k:
        if len(freq_list[i]) is 0:
            i -= 1
            continue
        
        for num in freq_list[i]:
            res.append(num)
            j += 1
        
        i-= 1

    return res


print(topKFrequent([1,1,1,2,2,3], 2))
