"""
Question:   
    https://leetcode.com/problems/remove-linked-list-elements/?envType=problem-list-v2&envId=recursion
"""


'''
Normal Solution

'''
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]

        curr -> head

        prev -> head

        swapping in linkedList:
            we move with head
                if head.val == val:
                    head = head.next
                    prev.next = head
                    prev = head


        if curr
        """

        start = prev = ListNode(next=head)

        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return start.next 

'''
Recursive Solution:
    
'''

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        if not head:
            return None
        
        head.next = self.removeElements(head.next, val)
        
        return head.next if head.val == val else head