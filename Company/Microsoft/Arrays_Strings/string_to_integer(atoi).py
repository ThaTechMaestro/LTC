class Solution(object):

'''
Follow the key implementations
    Use of rlen
    Use of ord
    Use of pow

'''
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #Remove leading whitespaces
        s = s.lstrip()
        MAX_INT = pow(2,31) -1
        MIN_INT = -pow(2,31)
        
        # Empty input Edge case
        if len(s) == 0:
            return 0
        
        
        start = 0
        sign_multiplier = 1
        
        
        # Implementing the correct sign
        if s[0] == "-":
            sign_multiplier = -1
            start = 1
        elif s[0] == "+":
            start = 1
        
        result = 0
        index = start
        
        
        while index < len(s):
            #When we come across non numeric value
            if not ('0' <= s[index] <= '9'):
                return result * sign_multiplier
            
            # Use of ASCII to get the required integer value
            # Then the multiplier, to get the successive value froom right to left
            result = (result * 10) + (ord(s[index]) - ord('0'))
            
            
            # Exceed Range Conditions
            if (result*sign_multiplier) <= MIN_INT:
                return MIN_INT
            elif (result*sign_multiplier) >= MAX_INT:
                return MAX_INT
            
            index +=1
        
        return result*sign_multiplier
 