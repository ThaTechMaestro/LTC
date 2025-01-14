'''
Interview based Solution

Insight:
    Use the split function
    Then reverse using two pointers
    return a string with join function
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        #it splits the string into a list by using argument passed
        s = s.split(" ")           

        i,j = 0,len(s)-1                #taking two pointers i and j where i starts from 0th index and j starts from last index
        while i < j:
            s[i],s[j] = s[j],s[i]       #swapping done
            i+=1
            j-=1
        s = " ".join(s)                 
        return s



'''
Using python Sugar
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        s = s.split()
        
        s.reverse()
        
        return " ".join(s)




Leetcode based Solution
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")                #it splits the string s
        while "" in s:                  #it removes all the spaces from the s
            s.remove("")
        print(s)
        i,j = 0,len(s)-1                #taking two pointers i and j where i starts from 0th index and j starts from last index
        while i < j:
            s[i],s[j] = s[j],s[i]       #swapping done
            i+=1
            j-=1
        s = " ".join(s)                 
        return s