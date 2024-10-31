'''
Question
https://www.designgurus.io/course-play/grokking-data-structures-for-coding-interviews/doc/problem-1-balanced-parentheses-easy

'''

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
                