"""
Time complexity: O(n)
Space complexity: O(n)

"""

def two_sum(self, nums, target):

    a_map = {}

    for i in range(len(nums)):
        res = target - nums[i]

        if res in a_map:
            return [a_map[res], i]
        a_map[nums[i]] = i