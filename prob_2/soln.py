class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        
        target value
        natural value 
        target = natural + unknown
        
        unknown = target - natural
        
        Possible questions I can ask:
            Are all the numbers within the array distinct
            Are there repeated values at different indexes within the array
            What should I return when I do not find elements that do not add up to a target
        
        This questions shows two things:
        Two pointers helps in using the same data structure
        It also shows the downside of using a map, when lookups are performed where
            repeated values are stored at different indexes.
            Maps work best with distinct values
        
        """
        
        
        left_index = 0
        right_index = len(numbers)-1
        
        left_index, right_index = 0, len(numbers)-1
        
            
        while left_index<right_index:
            left_pointer = numbers[left_index]
            right_pointer = numbers[right_index]
            
            sum = left_pointer + right_pointer
            
            if target == sum:
                return [left_index+1, right_index+1]
            
            if target > sum:
                left_index+=1
            else:
                right_index-=1
            
        
        return [-1, -1]