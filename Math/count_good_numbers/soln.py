'''
Question
    https://leetcode.com/problems/count-good-numbers/solutions/1314434/python-logarithmic-time-solution/?envType=problem-list-v2&envId=recursion

Helpful, related soln:
    https://leetcode.com/problems/count-good-numbers/solutions/1314434/python-logarithmic-time-solution/?envType=problem-list-v2&envId=recursion
'''

class Solution(object):
    
    '''
    Iterative Soln
    '''
    def countGoodNumbers(self, n):
        """
        Problem: Count Good Numbers
        Given an integer `n`, return the total number of good digit strings of length `n`,
        where:
        - Even indices (0-based) contain an even number (0, 2, 4, 6, 8).
        - Odd indices contain a prime number (2, 3, 5, 7).
        - Since the answer may be large, return it modulo (10^9 + 7).

        Step 1: Identify Key Concepts Needed
        - Modular Exponentiation: Needed for efficient calculation of large powers.
        - Even & Odd Index Pattern: Even indices have 5 choices, odd indices have 4.
        - Power Calculation: Since choices repeat every two positions, we use exponentiation.
        
        Step 2: Break Down the Solution Approach
        - Compute the number of valid choices for even and odd indices.
        - If `n` is even, the number of ways is `pow(20, n/2, MOD)`.
        - If `n` is odd, we multiply by 5 for the additional even index.
        
        Step 3: Implement the Code
        """
        MOD = 10**9 + 7  # Define modulo constant
        ans = pow(20, n // 2, MOD)  # Compute base cases efficiently
        
        if n % 2 == 1:
            ans = (ans * 5) % MOD  # Multiply by 5 if `n` is odd
        
        return ans
        
        """
        Step 4: Optimize and Improve
        - Time Complexity: O(log n) due to modular exponentiation.
        - Space Complexity: O(1) since only a few variables are used.
        
        Step 5: Follow-Up Questions to Deepen Understanding
        1. How would the approach change if more digits were allowed?
        2. Can this be solved iteratively instead of using `pow`?
        3. What if `n` was extremely large (e.g., 10^18)? How would efficiency be affected?
        4. How does modular arithmetic help in this problem?
        """
