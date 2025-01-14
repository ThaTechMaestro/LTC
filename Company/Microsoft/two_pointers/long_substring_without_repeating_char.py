class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        seen = {}
        left, right = 0,0
        result = 1
        '''
        Using the input index for my solution
        Dictionary -> to keep track of seen characters and their respective indexes
        
        
        '''
        while right < len(s):
            
            if s[right] in seen:
                
                #Update the left part of our window
                left = max(left, seen[s[right]]+1)
            
            #Calculate result
            result = max(result, right-left+1)
            
            #Update the dictionary seen character index
            seen[s[right]] = right
            
            #Update the right part of our window
            right += 1
        
        
        return result
 