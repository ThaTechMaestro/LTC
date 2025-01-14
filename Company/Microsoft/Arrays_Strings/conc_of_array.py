# https://leetcode.com/problems/concatenation-of-array/

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        
        Given 
        nums  
        n - len(nums)
        
        You created 
        ans
        len(ans) = 2 * len(nums)
        
        ans[]
        """
    
    
        
        return nums + nums

    
    def getConcatenation(self, nums):
        res = [0] * (len(nums) * 2)
        i, j = 0, len(nums)
        while j < len(res):
            res[i] = res[j] = nums[i]
            i += 1
            j += 1
        return res