'''
Question
https://www.designgurus.io/course-play/grokking-data-structures-for-coding-interviews/doc/problem-1-balanced-parentheses-easy

'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Original Solution:
        - Time Complexity: O(n), where n is the length of the string `s`. We iterate through each character exactly once.
        - Space Complexity: O(n), where n is the number of characters in the string. In the worst case, the stack will store all the opening brackets.
        """
        hm = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stk = []

        # Edge case: If the string has a single character, it cannot form a valid pair
        if len(s) == 1:
            return False

        for strg in s:
            if strg in hm.keys():
                stk.append(strg)
            elif len(stk) == 0 or hm[stk.pop()] != strg:
                return False

        return len(stk) == 0


    def isValidOptimized1(self, s):
        """
        Optimized Solution 1:
        - Time Complexity: O(n), where n is the length of the string `s`. We process each character in the string once.
        - Space Complexity: O(n), as the stack can hold all the opening brackets in the worst case.
        - This solution adds a quick check for odd-length strings (odd-length strings cannot have valid pairs).
        """
        hm = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stk = []

        # Edge case: If the string has an odd length, it cannot form valid pairs
        if len(s) % 2 != 0:
            return False 

        for strg in s:
            if strg in hm: 
                stk.append(strg)
            elif len(stk) == 0 or hm[stk.pop()] != strg:
                return False

        return len(stk) == 0 


    def isValidOptimized2(self, s):
        """
        Optimized Solution 2:
        - Time Complexity: O(n), where n is the length of the string `s`. We process each character in the string once.
        - Space Complexity: O(n), as the stack can hold all the opening brackets in the worst case.
        - This solution does not need any extra checks beyond the core logic, making it simpler and more efficient.
        """
        hm = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stk = []

        for strg in s:
            if strg in hm:
                stk.append(strg)
            elif len(stk) == 0 or hm[stk.pop()] != strg:
                return False

        return not stk 



class Solution:
    
    
    '''
    How do I know when a parenthesis is the opening or closing one
    
    Is there any meta-data I can use?
    Meta data:
        They are string
        They are symbols
        
    You need to use a matching dictionary
    '''
    
    def IsParenthesisBalanced(self, s):
        matching_parenthesis = {'}':'{', ')':'(', ']':'['}
        stack = []
        
        for c in s:
            
            if c in matching_parenthesis.values():
                stack.append(c)
            elif c in matching_parenthesis:
                if not stack or matching_parenthesis[c] != stack[-1]:
                    return False 
                stack.pop()
        
        return True
                