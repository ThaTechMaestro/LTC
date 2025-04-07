'''
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
def twoSum(self, numbers, target):
        """
        Problem: Two Sum II - Input Array Is Sorted (LeetCode 167)
        Given a 1-indexed array of integers sorted in non-decreasing order, find two numbers such that they add up to a specific target.
        Return the indices of the two numbers (1-indexed).

        Step 1: Identify Key Concepts Needed
        - Two Pointers: Efficient for sorted arrays where movement depends on comparison.
        - Sorted Array Properties: Enables decision-making to adjust pointers based on current sum.

        Step 2: Break Down the Solution Approach
        - Start two pointers: one at the beginning (left), one at the end (right).
        - Calculate the sum of elements at the two pointers.
        - If the sum equals the target, return their indices.
        - If the sum is greater, decrement the right pointer to reduce the sum.
        - If the sum is smaller, increment the left pointer to increase the sum.

        Step 3: Implement the Code
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left + 1, right + 1]  # Return 1-indexed positions
            elif result > target:
                right -= 1
            else:
                left += 1

        """
        Step 4: Optimize and Improve
        - Time Complexity: O(n), where n is the length of the array.
        - Space Complexity: O(1), no additional space is used.

        Step 5: Follow-Up Questions to Deepen Understanding
        1. What if duplicates are allowed—how would that affect the approach?
        2. Could we solve this using binary search? When would that be better?
        3. How would we adapt this if the array wasn’t sorted?
        4. Can this method be generalized for finding three numbers?

        Patterns to Take to Future Problems:
        - Two Pointers: Extremely useful on sorted arrays to find pairwise conditions.
        - Sliding Window: Related technique for problems involving ranges or subarrays.
        - Greedy Movement: Adjusting pointers based on feedback from conditions.
        """