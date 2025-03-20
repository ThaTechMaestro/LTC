'''
QUESTION:   
    https://leetcode.com/problems/elimination-game/?envType=problem-list-v2&envId=recursion
'''
class Solution(object):
    def lastRemaining(self, n):
        """
        This is MATHS & IT HAS A FORMULA, NO SUPER LOGIC
        
        Problem: Last Remaining Element (Elimination Game)
        Given an integer `n`, return the last remaining number after repeatedly removing
        every second number from a list of numbers from 1 to `n`.

        Step 1: Identify Key Concepts Needed
        - Recursion: The problem follows a recursive pattern where each step reduces `n`.
        - Mathematical Pattern: The remaining element follows a specific formula.
        - Even/Odd Handling: The elimination strategy depends on whether `n` is even or odd.
        
        Step 2: Break Down the Solution Approach
        - Base Case: If `n == 1`, return 1 (only one number left).
        - Recursive Step: The result follows the formula:
          `2 * (n / 2 + 1 - lastRemaining(n / 2))`
          where we map the reduced sequence back to the original sequence.
        
        Step 3: Implement the Code
        """
        if n == 1:
            return 1
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))
        
        """
        Step 4: Optimize and Improve
        - Time Complexity: O(log n) due to the recursive halving of `n`.
        - Space Complexity: O(log n) due to recursive stack depth.
        
        Step 5: Follow-Up Questions to Deepen Understanding
        1. Can this be solved iteratively instead of recursively?
        2. What is the mathematical intuition behind the recurrence relation?
        3. How would this change if we eliminated every third number instead of every second?
        4. How does this relate to binary representations or power of twos?
        """
