'''
Valid Palindrome - Problem 125


Question:

How do you check if it is a palindrome:
    Two pointer pattern

    Compare the first and last indexes since it contains non-alphanumerics
        and you can skip the non alpha-numerics with a condition
What should I return if it is an empty string:
    Return True

With Strings or arrays:
    There are odd and even lengths, how do you handle them
        It does not matter here, we do not need the middle

Solutions:
- Convert uppercase to lowercase
- Avoid all symbols and spaces
'''


'''
PATTERN:
    Two Pointer Pattern
    A palindrome is the same word
        which reads the same after being reversed -> This is why two pointer is optimal

INSIGHT:

    The key is:
        The first and last element of the palindrome should be the same
            And this should happen for subsequent values as the pointer
            approach one another
    
    In this case the length of the palindrome does not matter:
        If it is even:
            It means we were able to succesfully check all the elements in the array
            before the pointers passes each other, no meeting point

        If it is odd:
            It means all elements in the array can be succesfully checked,
            There will be a meeting point, which in the question the purpose of meeting point is not needed
            since both pointers will point to the same value at the end of the day


    The non-alpha numerics can be skipped, do not try to remove them
        They do not matter (It saves time)       

    Do not forget to increment your two pointers!
    
MISTAKES:
    Forgetting to increment pointers

    Wrong implementation of increasing the pointers
        first_pointer should be +=1
        second_pointer should be -=1

     Forgetting to convert individual string values
        to either upper or lower for uniformity during comparison   

Test:
    Do not forget empty input edge case

    Edge Test case:
        a man, a plan, a canal, Panama
        race a car

'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        first_pointer = 0
        second_pointer = len(s)-1
        
        if not s:
            return True
        
        while first_pointer < second_pointer:
            
            #Skip non-alpha numeric
            if not s[first_pointer].isalnum(): 
                first_pointer+=1
                continue
            
            #Skip Non-alpha numeric
            if not s[second_pointer].isalnum():
                second_pointer -=1
                continue
            
            #Convert to lowercase for uniformity and make comparison
            if s[first_pointer].lower() != s[second_pointer].lower():
                return False
            
            first_pointer +=1
            second_pointer -=1
        
        
        
        return True
   
