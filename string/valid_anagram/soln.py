'''
Question
    https://leetcode.com/problems/valid-anagram/description/

Follow Up:
    Can you implement your own custom sorting function?
    What if the inputs contain Unicode characters? 
        How would you adapt your solution to such a case?
    
'''

class Solution(object):
   
    """
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    

    Args:
        object (_type_): _description_
    """
    
    def isAnagram(self, s, t):
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        return s == t


