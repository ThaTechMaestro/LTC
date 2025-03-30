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


'''
Resolved
'''

class Solution(object):
    def decodeString(self, s):
        """
        Problem: Decode String (LeetCode 394)
        Given an encoded string, return its decoded version.
        The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
        is repeated exactly k times.

        Step 1: Identify Key Concepts Needed
        - Stack: Ideal for handling nested structures and reversing order.
        - String Manipulation: To extract and repeat substrings.
        - Digit Parsing: Extract multi-digit repetition counts.

        Step 2: Break Down the Solution Approach
        - Traverse each character of the string.
        - Push non-closing bracket characters onto the stack.
        - On encountering ']', pop characters to build the substring.
        - Pop digits to determine repetition count.
        - Multiply the substring and push it back on the stack.
        
        Step 3: Implement the Code
        """
        stk = []  # Stack to store characters and intermediate results

        for i in s:
            if i != "]":
                stk.append(i)
            else:
                # Extract substring to repeat
                sub_str = ""
                while stk and stk[-1] != '[':
                    sub_str = stk.pop() + sub_str

                # Remove the '['
                stk.pop()

                # Extract the repetition count
                num = ""
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num

                # Repeat the substring and add to stack
                stk.append(int(num) * sub_str)

        return "".join(stk)

        """
        Step 4: Optimize and Improve
        - Time Complexity: O(n), where n is the length of the input string.
        - Space Complexity: O(n), due to the use of a stack to hold characters.

        Step 5: Follow-Up Questions to Deepen Understanding
        1. How would the function behave with invalid input or malformed brackets?
        2. Could the same logic be implemented using recursion?
        3. What if the encoded string is extremely large or deeply nested?
        4. How does the stack ensure correct evaluation order?
        """