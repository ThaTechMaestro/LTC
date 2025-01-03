'''
Question
https://leetcode.com/problems/running-sum-of-1d-array/description/


Solutions based on Preference (Sorted by Most Votes):
1 - https://leetcode.com/problems/running-sum-of-1d-array/solutions/3167663/simple-solution-javacpppythonc-language-twlf4/


Concept:
Array modification in place using input array in one Pass
i.e Work on the same input array and modify it in place to contain the desired output
'''

class Solution:
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # SOLUTION 1
        # arr =[]
        # sum = 0

        # for i in range(len(nums)):
        #     if i==0:
        #         sum = nums[i]
        #         arr.append(sum)
        #         continue
        #     sum += nums[i]
        #     arr.append(sum)
        
        # return arr

        # OPTIMAL SOLUTION, modify inplace
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums