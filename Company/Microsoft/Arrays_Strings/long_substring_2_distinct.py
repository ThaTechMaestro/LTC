'''
Longest substringb with at most 2 distinct characters
'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ## RC ##
        ## APPROACH : SLIDING WINDOW ##
        ## Similar to Leetcode : 424. Longest Repeating Character Replacement ##
        ## Similar to Leetcode : 904. Fruit Into Basket ##
        ## SAME CODE : 340. Longest Substring with At Most K Distinct Characters ##
		
        ## TIME COMPLEXICITY : O(N) ##
		## SPACE COMPLEXICITY : O(N) ##
        
        lookup = collections.defaultdict(int)
        n, k = len(s), 2
        start = end = max_len = 0 
        while(end < n ):
            lookup[ s[end] ] += 1
            end += 1
            while( len(lookup) > k ):
                lookup[ s[start] ] -= 1
                if( lookup[ s[start] ] == 0 ):
                    del lookup[ s[start] ]
                start += 1
            max_len = max( max_len, end - start )        
        return max_len


        lookup = collections.defaultdict(int)
        start = end = max_length = 0

        while (end < len(s)):

            lookup[s[end]] += 1
            end += 1

            while(len(lookup) > k):
                lookup[ s[start]] -= 1

                if(lookup[s[start]] == 0):
                    del lookup[s[start]]
                    
                start += 1


            max_len = max(max_len, end-start)

