class Solution:

    def get_length_of_longest_substring(self, s):

        if len(s) == 0:
            return 0
        

        max_length = 1
        left, right = 0, 0
        dictionary = {}

        while right < len(s):

            if s[right] in seen:
                left = seen[s[right]] + 1
                pass 
            
            max_length = max(max_length, right-left+1)
            seen[s[right]] = right 
            right -= 1
        
        return max_length
        pass 

# Edge test case ----> abba


class Solution:

    def get_length_of_longest_substring(self, s):

        if len(s) == 0:
            return 0
        

        max_length = 1
        left, right = 0, 0
        dictionary = {}

        while right < len(s):

            if s[right] in seen:
                left = seen[s[right]] + 1

            
            max_length = max(max_length, right-left+1)
            seen[s[right]] = right 
            right += 1
        
        return max_length
