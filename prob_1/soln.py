def two_sum(self, nums, target):

    a_map = {}

    for i in range(len(nums)):
        res = target - nums[i]

        if res in a_map:
            return [i, a_map[res]]
        a_map[nums[i]] = i