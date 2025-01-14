class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left,right = 0, len(height)-1
        l_max,r_max = 0,0
        answer = 0
        
        while left < right:
            
            #Get the lowest bounded height from the two pointers indexes
            if height[left] < height[right]:
                
                if height[left] >= l_max:
                    l_max = height[left]
                else:
                    answer += l_max - height[left]
                    
                left += 1
            else:
                
                if height[right] >= r_max:
                    r_max = height[right]
                else:
                    answer += r_max - height[right]
            
                right -= 1
        
        return answer