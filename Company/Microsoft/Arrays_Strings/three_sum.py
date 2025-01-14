
'''
PERFECT SOLUTION

Edge cases Input:
    nums = [0, 0, 0]

Possible Follow Up:
    What if you cannot sort the array:
        A memory efficient

'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        
        #nums.sort returns None when assigned to a variable, use it in place
        nums.sort()
        print(nums)
        
        for index, first_value in enumerate(nums):
            
            #This is a game changer for cutting through a very large array
            #There is no point checking through elements, with first index being positive
            #   when the first array is sorted
            if nums[index] > 0:
                break
                
            if index > 0 and first_value == nums[index-1]:
                continue
            
            left_index, right_index = index+1, len(nums)-1
            
            while left_index < right_index:
                
                three_sum = first_value + nums[left_index] + nums[right_index]

                
                if three_sum > 0:
                    right_index -= 1
                elif three_sum < 0:
                    left_index += 1
                else:
                    result.append([first_value, nums[left_index], nums[right_index]])
                    left_index += 1
                    
                    #The second condition after and, is to prevent and out of range exception
                    while(nums[left_index] == nums[left_index-1] and left_index < right_index):
                        left_index +=1
                
                
        return result


'''
https://leetcode.com/problems/3sum/discuss/514346/Python-~95-Solution-Commented-and-Explained
Look at the solution for following up by using the no sorting approach
'''

def three_Sum(nums):

  result = set()

  array_length = len(nums)

  for first_index in range(array_length):
    hash_set = set()


    for second_index in range(first_index+1, array_length):

      print()
      first_value, second_value = nums[first_index], nums[second_index]
      print("First value ",first_value )
      print("Second Value", second_value)
      third_value = -first_value-second_value
      print("Third value ", third_value)
      print("Hash set ", hash_set)
      

      if third_value in hash_set:
        result.add(tuple(sorted([first_value, second_value, third_value])))
        print("Result: ", result)
        print()

      #Why?
      hash_set.add(second_value)
      print("Hash_set for new iteration ", hash_set)


    return [list(result) for collection in result]


print(three_Sum(nums))

#lEETCODE sOLUTION TO THIS QUESTION ALSO MAKES SENSE
