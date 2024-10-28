'''
Question
    https://www.designgurus.io/course-play/grokking-data-structures-for-coding-interviews/doc/problem-2-matrix-diagonal-sum-easy

'''

class Solution:
    '''
    Hint: 
        Diagonal are those elements (where row & column index are equal)
            For the left to right
            
        What about right to left?
    '''
    
    def get_sum_of_diagonal_elements(self, arr):
        diagonal_sum = 0
        
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                
                if i != j:
                    continue
                
                diagonal_sum += arr[i][j]
        
        print(diagonal_sum)
        return diagonal_sum
    
    '''
    OPTIMAL SOLUTION
        This is way better
    '''
    def fetch_sum_of_diagonal_elements(self, arr):
        n = len(arr)
        diagonal_sum = 0
        
        for i in range(n):
                diagonal_sum += arr[i][i] + arr[i][n-i-1]
        
        if n % 2 != 0:
            diagonal_sum -= arr[n//2][n//2]
            
        print(diagonal_sum)
        return diagonal_sum


arr = [[1,2,3],[4,5,6],[7,8,9]]
soln = Solution()
soln.get_sum_of_diagonal_elements(arr)
soln.fetch_sum_of_diagonal_elements(arr)