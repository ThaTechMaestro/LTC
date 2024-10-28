class Solution:
    
    '''
    APPROACH 1
    This one wwas pretty straightforward
        Completely test the code in your head before running
        
        Caveats: I used extra space
    '''
    def get_max_height(self, height_diff_array):
        max_height = 0
        heights_array = [0]*len(height_diff_array)
        current_height = 0
        
        for i in range(len(height_diff_array)):           
            current_height += height_diff_array[i]
            heights_array[i] = current_height
        
        if max_height >= max(heights_array):
            return max_height
        
        return max(heights_array)
    
    '''
    APPROACH 2
    OPTIMAL VERSION: No extra space complexity
    
    Time Complexity: O(N)
    Space Complexity: 0(1)
    '''
    def fetch_max_height(self, height_diff_array):
        max_height = 0
        current_height = 0
        
        for diff in height_diff_array:           
            current_height += diff
            max_height = max(max_height, current_height)
        
        return max_height

a = [1,2,3,4,5]
soln = Solution()
print(soln.get_max_height(a))
print(soln.fetch_max_height(a))