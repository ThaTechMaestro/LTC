'''
Question:
    https://leetcode.com/problems/decode-string/description/?envType=problem-list-v2&envId=recursion
'''

'''
Iterative Solution
'''
def decodeString(self, s):
    """
    :type s: str
    :rtype: str

    The idea is to use a stack
        why? Its best suited for 
    """

    stk = []
    for i in range(len(s)):
        '''
        [

        ]
        '''

        if s[i] != "]":
            stk.append(s[i])
        else:
            substr = ""

            '''
            what is meant to happen here
                we are to use the value in the stk
                I have the substring
            '''
            while stk and stk[-1] != "[":
                substr = stk.pop() + substr
            
            print(substr)
            stk.pop()

            '''
                I have the integer or value
            '''
            k = ""
            while stk and stk[-1].isdigit():
                k = stk.pop() + k
            stk.append(int(k)*substr)
    
    return "".join(stk)