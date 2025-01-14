class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        Technique -> Expand from the centre
        Perform the check sequentially for odd numbered string length and even numbered string length

        Time Complexity -> 0(n^2)
        """
        
        result = ""
        result_length = 0
        
        if len(s) == 1 or not s:
            return s
        
        
        for i in range(len(s)):
                
                #Odd numbered
                left, right = i,i
                
                #Index validation check
                # Odd numbered -> It takes the longest sub-palindrome, assuming legth it odd
                while (left >= 0 and right < len(s) and s[left] == s[right]):
                    #Longest palindrom substring check
                    if ((right - left + 1) > result_length):
                        
                        result = s[left:right+1]
                        result_length = right - left + 1
                        
                    left -= 1
                    right += 1
                
                
                #even numbered
                left, right = i,i+1
                
                #Index validation check
                # It compares the result, sequentially, with the assumption it is even
                while (left >= 0 and right < len(s) and s[left] == s[right]):
                    #Longest palindrom substring check
                    if ((right - left + 1) > result_length):
                        
                        result = s[left:right+1]
                        result_length = right - left + 1
                        
                    left -= 1
                    right += 1
        
                
                
        return result