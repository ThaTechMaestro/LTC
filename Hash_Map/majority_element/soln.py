'''
Question:
https://leetcode.com/problems/majority-element/
'''


# Naive Solution: Hash Map Frequency Count
# Time: O(n), Space: O(n)
# Tracks frequencies of elements using a hash map.
class Solution:
    def majorityElement(self, nums):
        freq = {} 
        for x in nums:
            freq[x] = freq.get(x, 0) + 1 
            if freq[x] > len(nums) // 2: 
                return x  

        # max_count = 0
        # max_elem = 0
        # hash_map = {}

        # for x in nums:
        #     hash_map[x] = 1 + hash_map.get(x, 0)

        #     if hash_map[x] > max_count:
        #         max_count = hash_map[x]
        #         max_elem = x
        
        # return max_elem
            

class Solution:
    def majorityElement(self, nums):
        """
        Optimal Solution: Boyer-Moore Voting Algorithm
        Time: O(n), Space: O(1)
        Tracks a candidate majority element and adjusts the count based on matches/differences.
        """
        max_elem, max_count = 0, 0
        for x in nums:
            if max_count == 0:  # Reset candidate when count is zero
                max_elem, max_count = x, 1
            elif x == max_elem:  # Increment count if it matches the candidate
                max_count += 1
            else:  # Decrement count if different
                max_count -= 1
        return max_elem  # Candidate is guaranteed to be the majority element


        '''
        >>>More concise
        
        
        max_elem, max_count = 0, 0
        for x in nums:
            # Reset candidate if count is zero
            max_count += 1 if max_count == 0 or x == max_elem else -1
            if max_count == 1:  # Update candidate when count is reset
                max_elem = x
        return max_elem
        '''

