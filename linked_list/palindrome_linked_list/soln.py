def isPalindrome(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: bool

    Steps:
    1. Find the middle using fast & slow pointers
    2. Reverse the second half of the linked list
    3. Compare first half and reversed second half
    4. Restore list (optional)
    5. Follow-up questions to deepen understanding
    """

    if not head or not head.next:
        return True  # Edge case: An empty or single-node list is always a palindrome

    # Step 1: Find the middle of the linked list
    # Use fast and slow pointers. Fast moves 2 steps, slow moves 1 step.
    # When fast reaches the end, slow will be at the middle.
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    # We reverse the second half in-place to compare it with the first half.
    prev, curr = None, slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Step 3: Compare both halves
    # Compare the first half (starting from head) and the reversed second half (starting from prev).
    head1, head2 = head, prev
    while head2:  # Only need to check the second half
        if head1.val != head2.val:
            return False  # Mismatch found, not a palindrome
        head1 = head1.next
        head2 = head2.next 

    # Step 4: (Optional) Restore the second half of the list to its original form
    # Some interviewers expect you to restore the list after checking.
    # Reverse the second half again to bring it back to its original order.
    prev, curr = None, slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return True  # If no mismatches were found, the list is a palindrome

    """
    Step 5: Follow-Up Questions (For deeper understanding)
    1. What happens if the linked list is a doubly linked list? Would our approach change?
    2. How would we solve this problem using recursion instead of iteration?
    3. What if the linked list is extremely large? Would an O(n) space approach be acceptable?
    4. Can we solve this problem in O(n log n) time? Would that be useful?
    5. How do we modify this approach to restore the original list structure after checking?
    """

