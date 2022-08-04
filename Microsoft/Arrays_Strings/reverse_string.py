'''
Recursive Solution

Mistakes:
        Do not perform increment of pointers in recursive method impl

'''

class Solution(object):
        
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        
        Mistakes:
            Do not perform increment of pointers in recursive method impl
            
        """

        def reverse_impl(left_pointer, right_pointer):

            if left_pointer >= right_pointer:
                return 

            s[left_pointer],s[right_pointer] = s[right_pointer], s[left_pointer]
            reverse_impl(left_pointer+1, right_pointer-1)
        

        left_pointer = 0
        right_pointer = len(s)-1

        reverse_impl(left_pointer, right_pointer)
#---------------------------------->----------------------->---------------------------------------------
'''
Two Pointer Solution

'''

'''
Iterative Solution

Use this Solution when given input is not an array

'''

class Solution:
    def reverseString(self, s):

      
        s  = list(s)
        '''
        Converting to a list because we can not
         modify string values:
        It is immutable

        But it uses O(n) space
        '''
        left, right = 0, len(s) - 1

      
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

        return s


'''
Iterative Solution

Use this Solution when given input is an array
    
'''

class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
