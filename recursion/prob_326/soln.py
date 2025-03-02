'''
Question:
    https://leetcode.com/problems/power-of-three/?envType=problem-list-v2&envId=recursion
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and 3**19 % n == 0
    