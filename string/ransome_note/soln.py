'''
Question

https://leetcode.com/problems/ransom-note/description/
    
'''

from collections import defaultdict, Counter

# Original Solution
# This solution uses `defaultdict(int)` to count characters in the magazine
# and then checks if each character in the ransom note can be found in the magazine.
class Solution:
    def canConstruct_original(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool

        Time Complexity: O(m + n), where m = length of ransomNote, n = length of magazine.
        Space Complexity: O(n), where n = length of magazine (for storing character counts).

        Downsides:
        1. Manual counting of characters with explicit loops.
        2. Space usage could be high if the magazine is large.
        3. Less concise code due to explicit decrements.
        """
        dict2 = defaultdict(int)  # Default value for missing keys is 0.

        # Count each character in the magazine.
        for char in magazine:
            dict2[char] += 1

        # Check if ransomNote can be constructed from magazine.
        for char in ransomNote:
            if dict2[char] < 1:  # If not enough occurrences of char.
                return False
            dict2[char] -= 1  # Use up one occurrence.

        return True  # All characters are accounted for.


# **Optimized Solution 1:** Using `Counter`
# This solution simplifies the process by using the `Counter` class from `collections`.
class Solution:
    def canConstruct_optimized_1(self, ransomNote, magazine):
        """
        Time Complexity: O(m + n), where m = length of ransomNote, n = length of magazine.
        Space Complexity: O(n), for storing character counts in the Counter.

        Improvements:
        1. Automatic counting of characters using `Counter`, simplifying the code.
        2. Direct comparison of character counts using dictionary-like lookups.
        """
        magazine_count = Counter(magazine)
        ransom_note_count = Counter(ransomNote)

        # Check if all characters in ransomNote are present in sufficient quantity.
        for char, count in ransom_note_count.items():
            if magazine_count[char] < count:
                return False  # Return False if the magazine lacks enough characters.

        return True  # All characters have sufficient counts.


# **Optimized Solution 2:** Using `Counter` Subtraction
# This solution leverages `Counter` subtraction to directly check differences.
class Solution:
    def canConstruct_optimized_2(self, ransomNote, magazine):
        """
        Time Complexity: O(m + n), where m = length of ransomNote, n = length of magazine.
        Space Complexity: O(n), for the Counter objects.

        Additional Edge Case:
        1. Quick return if ransomNote is longer than magazine, since it is impossible.
        """
        if len(ransomNote) > len(magazine):
            return False  # Edge case: ransomNote cannot be longer than magazine.

        # Subtract counts and check if any characters are missing.
        return not (Counter(ransomNote) - Counter(magazine))  # If the result is empty, return True.


# Usage Example:
if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct_original("aa", "aab"))  # True
    print(solution.canConstruct_optimized_1("aa", "aab"))  # True
    print(solution.canConstruct_optimized_2("aa", "a"))  # False


""""
Sample of counter appleid on a string:
Counter({'s': 2, 'e': 2, 'a': 1, 'i': 1, 'n': 1, 'r': 1, 'k': 1})

"""
