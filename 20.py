"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    hash_map = {"(": ")", "{": "}", "[": "]"}
    opening_brackets = "({["

    for a in s:
        if a in opening_brackets:
            stack.append(hash_map[a])
        else:
            if len(stack) == 0:
                return False
            
            if stack.pop() == a:
                continue
            else:
                return False


    if len(stack) == 0:
        return True
    
    return False


