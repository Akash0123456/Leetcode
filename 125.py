"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    # Convert string to be only lowercase alphabets
    string = ""
    for c in s.lower():
        if c.isalpha() or c.isdigit():
            string += c
    
    if len(string) <= 1:
        return True
    
    start_ptr = 0
    end_ptr = len(string) - 1

    for i in range(len(string)):
        if start_ptr >= end_ptr:
            return True
        
        if string[start_ptr] == string[end_ptr]:
            start_ptr += 1
            end_ptr -= 1
        else:
            return False
    
    return False