'''
    Question:
        https://leetcode.com/problems/reverse-linked-list/?envType=problem-list-v2&envId=recursion
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        '''
        Normal
        '''
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev


        '''
        Recursive
        '''
        # if not head or not head.next:
        #     return head

        # new_head = self.reverseList(head.next)

        # head.next.next = head
        # head.next = None

        # return new_head
        