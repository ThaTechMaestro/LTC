class Solution(object):

    '''
    Use a Set
        It has a constant O(1) lookup time
    '''
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        first_pointer, second_pointer = 0, len(s)-1
        
        s = list(s)
        
        vowel_list = {'a','e','i','o','u','A','E','I','O','U'}
        
        if not s:
            return s
        
        
        while first_pointer < second_pointer:
            
            
            if s[first_pointer] in vowel_list and s[second_pointer] in vowel_list:
                s[first_pointer], s[second_pointer] = s[second_pointer], s[first_pointer] 
            
            elif s[first_pointer] not in vowel_list:
                first_pointer += 1
                continue
            elif s[second_pointer] not in vowel_list:
                second_pointer -= 1
                continue
            
            first_pointer +=1
            second_pointer -= 1
        
        return "".join(s)
   