# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.


"""
Find the length of the two words using len().
Set i and j to 0.
Create a while loop - as long as i < w1 or j < w2
Add the chars to the ans string if the value of i or the value of j is less than 
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        ans=""
        i=0
        j=0
        w1=len(word1)
        w2=len(word2)

        while i < w1 or j < w2:
            if i < w1:
                ans += word1[i]
                i += 1
            if j < w2:
                ans += word2[j]
                j += 1
        return ans


        