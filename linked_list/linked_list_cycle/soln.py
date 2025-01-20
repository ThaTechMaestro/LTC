'''
Question
https://leetcode.com/problems/linked-list-cycle/description/

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1(Personal): Using a Set to Track Node References
def hasCycle_set(self, head):
    """
    Detects cycle using a set to track node references.
    
    Time Complexity: O(n)  
    Space Complexity: O(n)  
    
    Issue:
        Time complexity exceeded as Set can grow very large
    """
    seen = set()  # Initialize a set to store nodes we've already seen
    curr_pointer = head

    # Traverse the list
    while curr_pointer:
        if curr_pointer in seen: 
            return True
        seen.add(curr_pointer) 
        curr_pointer = curr_pointer.next 

    return False 

# Optimized Solution: Floyd's Tortoise and Hare Algorithm
def hasCycle_floyd(self, head):
    """
    Detects cycle using two pointers: slow (tortoise) and fast (hare).
    
    Time Complexity: O(n)  
    Space Complexity: O(1)  
    """
    if not head or not head.next:  # Edge case: empty list or single node
        return False

    slow = head  
    fast = head  

    # Traverse the list with two pointers
    while fast and fast.next:
        slow = slow.next         
        fast = fast.next.next    

        if slow == fast: 
            return True

    return False 
