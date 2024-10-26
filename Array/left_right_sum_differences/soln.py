'''
Problem Link: 
https://leetcode.com/problems/left-and-right-sum-differences/
https://www.designgurus.io/course-play/grokking-data-structures-for-coding-interviews/doc/problem-3-left-and-right-sum-differences-easy
'''

class Solution:
    
    '''
    APPROACH 1
    
    My First approach is using loop + array slicing
            Which is just the normal way I think
            It is a reflection of how I currently think towards problem solving
    
    '''
    def get_difference_array(self, nums):
        
        diff_array = []
        
        for i in range(len(nums)):
            
            left_sum = sum(nums[:i])
            if i != len(nums) - 1:
                right_sum = sum(nums[i+1:])
            else:
                right_sum = 0
            
            diff_array.append(abs(left_sum - right_sum))
            print(diff_array)
            
    
    
    '''
    APPROACH 2
    
    The second approach in v2 is the optimal approach
        traversing once
    
    To traverse linear data strcuture once and solve a problem
        there would be a metadata somewhere,
        somewhere information I can use to solve the problem on the go
        
        The metadata here calculating the sum of all the elements
            in the array in advance
        
    '''
    def find_difference_array(self, nums):
        
        left_sum = 0
        right_sum = sum(nums)
        difference_array = []
        
        for i in range(len(nums)):
            
            right_sum -= nums[i]
            
            if i == 0:
                difference_array.append(abs(left_sum - right_sum))
                continue
            
            left_sum += nums[i-1]
            
            difference_array.append(abs(left_sum - right_sum))
        
        print(difference_array)
        return difference_array

'''
Test Cases
nums = [1,2,3,4,5]
'''

soln = Solution()
nums = [1,2,3,4,5]
# soln.get_difference_array(nums)
soln.find_difference_array(nums)

