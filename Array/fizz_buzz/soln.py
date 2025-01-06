'''
Question
    https://leetcode.com/problems/fizz-buzz/description/
'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]

        min of n = 1
        max of n = 10000

        output > n (an array containing strings)
        n is the length of the array, 
            but we want the first index as the starting point

        Solve, then ask:
            How can this be further improved?
        """

        '''
        Initial Solution:
            Cons - repeated use of modulo
            Cons - repeated use of append funciton- redundant

        answer = []
        for i in range(1,n+1):

            if ((i % 3 == 0) and (i % 5 == 0)):
                answer.append("FizzBuzz")
                continue
            if (i % 3 == 0):
                answer.append("Fizz")
                continue
            if (i % 5 == 0):
                answer.append("Buzz")
                continue
            answer.append(str(i))
            
        return answer
        '''
        

        """
        Without the use of modulo
        """
        answer = []
        fizz, buzz = 0, 0

        for i in range(1,n+1):
            fizz+=1
            buzz+=1
        
            if (fizz*buzz == 15):
                answer.append("FizzBuzz")
                fizz,buzz = 0,0
            elif (fizz == 3):
                answer.append("Fizz")
                fizz = 0
            elif buzz == 5:
                answer.append("Buzz")
                buzz = 0
            else:
                answer.append(str(i))

        return answer
            

        