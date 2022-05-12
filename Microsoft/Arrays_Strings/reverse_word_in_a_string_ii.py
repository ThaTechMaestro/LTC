'''
Use of Two pointers
and
a way to get new start for reversing

reverse the given array
then reverse subsequent elements in the array which can be grouped by a space
'''

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if not s:
            return s
        
        self.reverse_impl(s, 0, len(s)-1)
        
        
        new_start = 0
        for i in range(len(s)):
            
            if s[i] == " ":
                self.reverse_impl(s,new_start, i-1)
                new_start = i+1
            elif i == len(s)-1:
                self.reverse_impl(s, new_start, i)
                
                
        
        
    
    
    def reverse_impl(self, s, start, end):
        
        while start < end:
            
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1