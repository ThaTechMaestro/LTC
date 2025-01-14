# https://leetcode.com/problems/insert-interval/

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        
        for i in range(len(intervals)):

            '''
            Case 1
            The new interval does not pre-overlap
            Hence it never overlaps the remaining
            intervals in the interval List
            
            '''  
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:

                '''
                Case 2

                For a current interval in the interval list
            
                if the new interval does not post overlap
                Hence we add the current interval to the result 
                list
            
                But there is a high chance it overlaps with remaining 
                intervals in the interval list
            
                '''
                result.append(intervals[i])
                print(result)
            else:

                '''
                Case 3

                When there is an overlap
                We resolve the overlap
                Then set it to the new Interval, which is used to 
                    go through the remaining intervals list
                
                '''
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        result.append(newInterval)
        
        return result