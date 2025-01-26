'''
Question
https://leetcode.com/problems/happy-number/description/

Solve Normally,
Follow Up:
    Can this be solved in Constant Space?
'''


class Solution(object):
    def isHappy(self, n):
        """
        Original Solution: Using a Set to Track Seen Numbers
        Time Complexity: O(log(n)), Space Complexity: O(k) 
        where k is the number of unique numbers in the cycle.
        """
        seen = set() 
        
        while n not in seen:
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n)) 
            if n == 1:
                return True
        
        return False

    def isHappyOptimized(self, n):
        """
        Optimized Solution: Using Floyd's Cycle Detection
        Time Complexity: O(log(n)), Space Complexity: O(1)
        This eliminates the need for a set by using two pointers.
        """
        def get_next(number):
            # Compute the sum of squares of digits
            return sum(int(i) ** 2 for i in str(number))

        slow = n 
        fast = get_next(n) 

        while fast != 1 and slow != fast:  
            slow = get_next(slow)       
            fast = get_next(get_next(fast))

        return fast == 1 
