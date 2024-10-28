'''
Questions:
    https://www.designgurus.io/course-play/grokking-data-structures-for-coding-interviews/doc/problem-1-richest-customer-wealth-easy
    
'''

class Solution:
    
    '''
    OPTIMAL SOLN

        Time Complexity: O(m*n)
            m -> length of accounts
            n -> length of acct
        Space Complexity: O(1)
    '''
    def get_max_wealth(self, accounts):
        max_wealth = 0
        
        for acct in accounts:
            max_wealth = max(max_wealth, sum(acct))
        
        return max_wealth
        