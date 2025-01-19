'''
Question
    https://leetcode.com/problems/roman-to-integer/description/
    
    Problem description not super clear,
    Revisit this after a week
    
    No of times Resolved: 1
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        Original Solution (Iterating through the front):
        - The algorithm checks if the current Roman numeral is smaller than the next one to determine whether to add or subtract.
        - Time complexity: O(n), where n is the length of the input string `s`.
        - Space complexity: O(1), since only a dictionary and an integer are used.
        """
        store = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        for i in range(len(s)):
            if i + 1 < len(s) and store[s[i]] < store[s[i + 1]]:
                sum -= store[s[i]]  # Subtract the value if current is smaller than next
            else:
                sum += store[s[i]]  # Otherwise, add the value
        return sum

    def romanToIntOptimized1(self, s):
        """
        Optimized Solution 1 (Iterating from the back):
        - This solution iterates over the string in reverse order. It simplifies the check by only adding values and subtracting when a smaller value appears before a larger one.
        - Time complexity: O(n), where n is the length of the input string `s`.
        - Space complexity: O(1), as only the dictionary and a few variables are used.
        """
        store = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        prev_value = 0
        for i in range(len(s) - 1, -1, -1):  # Start from the end of the string
            curr_value = store[s[i]]
            if curr_value < prev_value:
                sum -= curr_value  # If current value is less than previous, subtract
            else:
                sum += curr_value  # Otherwise, add
            prev_value = curr_value  # Update previous value
        return sum

    def romanToIntOptimized2(self, s):
        """
        Optimized Solution 2 (More intuitive approach, forward iteration with condition):
        - This solution is similar to the original but cleans up redundant checks by ensuring we only check each character against the next one once.
        - Time complexity: O(n), where n is the length of the input string `s`.
        - Space complexity: O(1), as only a dictionary and an integer are used.
        """
        store = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        for i in range(len(s) - 1):  # Stop at second-to-last character
            if store[s[i]] < store[s[i + 1]]:
                sum -= store[s[i]]  # Subtract if current is smaller than next
            else:
                sum += store[s[i]]  # Otherwise, add
        sum += store[s[-1]]  # Add the value of the last character
        return sum
