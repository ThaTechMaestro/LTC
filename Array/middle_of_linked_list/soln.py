'''
Question
    https://leetcode.com/problems/middle-of-the-linked-list/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
         
        """
        
        """
        SOLUTION 1

        single_leap = head
        double_leap = head

        while True:
            if double_leap.next != None:
                if double_leap.next.next != None:
                    double_leap = double_leap.next.next
                    single_leap = single_leap.next
                    continue
                single_leap = single_leap.next
                return single_leap
            return single_leap

        """

        """
        OPTIMAL SOLUTION

        Handles empty input
            None input
        removed the use of nest if from Soln1
        
        TIME COMPLEXITY:
            O(n)
                It is actually O(n/2) since the double_leap
                takes 2 steps but approx O(n)

        
        SPACE COMPLEXITY:
            O(1)
                No additional data structure created
                The amount of memory used does not
                    depend on the size of the input LinkedList
        """

        single_leap = head
        double_leap = head

        while double_leap and double_leap.next != None:
            double_leap = double_leap.next.next
            single_leap = single_leap.next
            
        return single_leap


        