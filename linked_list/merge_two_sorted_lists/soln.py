'''
Question
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''

########################################
# Definition for singly-linked list.   #
########################################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


###################################################################
# Self (Naive) SOLUTION - Creates a New List (Extra Allocations)   #
###################################################################
def merge_two_lists_naive(list1, list2):
    """
    Naive Solution:
    - We iterate through both sorted lists simultaneously,
      but for each comparison, we create a NEW node to place into the result.
    - This leads to O(n+m) new allocations if total nodes = n + m.

    Time Complexity: O(n + m)
        We traverse each node from both lists exactly once.

    Space Complexity: O(n + m)
        We allocate a whole new list of size (n+m).

    Edge Cases:
    - If one list is empty, we simply copy the other list's nodes into the new list.
    - If both are empty, return None.
    - Handles duplicates by just taking whichever is smaller or from list2 if tie.
    """
    dummy = ListNode()  # New dummy head
    current = dummy

    # Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            # CREATE a new node (extra memory)
            current.next = ListNode(list1.val)
            list1 = list1.next
        else:
            current.next = ListNode(list2.val)
            list2 = list2.next
        current = current.next

    # If one list is exhausted, copy the rest of the other list
    while list1:
        current.next = ListNode(list1.val)
        list1 = list1.next
        current = current.next

    while list2:
        current.next = ListNode(list2.val)
        list2 = list2.next
        current = current.next

    return dummy.next


####################################################################
# OPTIMIZED SOLUTION #1 - Iterative, In-Place (No Extra Nodes)     #
####################################################################
def merge_two_lists_in_place(list1, list2):
    """
    In-Place Iterative Solution:
    - We reuse the existing nodes from both lists, linking them in a new merged sequence.
    - We compare the heads of each list, attach the smaller node to 'tail.next',
      and advance that list's pointer.

    Time Complexity: O(n + m)
        Each node in both lists is processed exactly once.

    Space Complexity: O(1)
        Aside from creating a dummy head node, no additional linked-list nodes are created.

    Edge Cases:
    - If list1 is empty, just return list2.
    - If list2 is empty, just return list1.
    - If both empty, returns None.
    - Automatically handles duplicates by whichever list head is smaller (or tie goes to the else branch).
    """
    dummy = ListNode()
    tail = dummy

    # Merge while both lists have nodes
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Attach whichever list still has nodes
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


#################################################################
# OPTIMIZED SOLUTION #2 - Recursive (Reuse Existing Nodes)      #
#################################################################
def merge_two_lists_recursive(list1, list2):
    """
    Recursive Solution:
    - Compare the heads of both lists; attach the smaller node,
      then recurse on the remainder.
    - We reuse the existing nodes, so no extra node allocations.

    Time Complexity: O(n + m)
        Each node is visited once. However, each call spawns a new function frame.

    Space Complexity: O(n + m)
        In the worst case, the call stack can go as deep as the total number of nodes.

    Edge Cases:
    - If one list is None, return the other list directly.
    - Works with duplicates by letting the else case handle ties.

    NOTE: In languages with limited stack memory, for very large lists, recursion might risk stack overflow.
    """
    # Base Cases
    if not list1:
        return list2
    if not list2:
        return list1

    # Recursive Step
    if list1.val < list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2


########################################
# END OF FILE                          #
########################################

