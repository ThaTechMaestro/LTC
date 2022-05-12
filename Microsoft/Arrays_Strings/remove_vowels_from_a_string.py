class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowel_list = set('AEIOUaeiou')
        result = []
        
        for i in s:
            if i not in vowel_list:
                result.append(i)
                
        return "".join(result)
  