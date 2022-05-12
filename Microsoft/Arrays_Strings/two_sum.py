'''
Name on Leetcode: Two Sum Problem

Identification: Sum Problem

array - nums 
int - target 
complement = {}


Loop through the array (using the index):
    if target - nums[i] == nums[i+1]:
        complement[i] = nums[i]


---->
PATTERN:
    Using a dictionary to keep track of previous elements
        that have been looped through in the arrray
        using value as the key and index as the value
Insight
- The key is to keep track of elements
    in the array we have passed through and their
    corresponding index using a dictionary

Test
- Do not forget the empty input edge case
- Do not forget to ask what the outputs are
    Leetcode own is returning indexes


Questions:
-> Is the array Sorted?

        If array is not sorted -> Use a dictionary (It helps keep track of elements we have passed while looping)
        If array is sorted -> Use Two Pointers
-> 

'''
def twoSum(self, nums, target):

    if not nums:
        return nums
    else:
        cache = {}

        for index, value in enumerate(nums):
            remainder = target - value 

            if remainder in cache:
                return [cache[remainder], index]
            else:
                cache[value]=index 

