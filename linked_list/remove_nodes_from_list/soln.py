class Solution(object):
    def removeNodes(self, head):
        """
        Problem: Remove Nodes From Linked List
        Given the head of a linked list, remove every node which has a node with a greater value anywhere to the right.

        Step 1: Identify Key Concepts Needed
        - Monotonic Stack: Helps maintain a decreasing sequence where each element has no greater value to its right.
        - Linked List Reconstruction: Once irrelevant nodes are removed, a new list is reconstructed from the filtered values.

        Step 2: Break Down the Solution Approach
        - Traverse the list while maintaining a decreasing stack of values.
        - If the current node has a value greater than elements in the stack, we pop those smaller elements.
        - Push the current node value onto the stack.
        - After traversal, rebuild the linked list from the values in the stack.

        Step 3: Implement the Code
        """
        stack = []  # Pattern 1: Monotonic Stack - maintain decreasing values

        while head:
            while stack and head.val > stack[-1]:  # Greedy elimination of smaller values
                stack.pop()
            stack.append(head.val)
            head = head.next

        dummy = ListNode()  # Pattern 2: Linked List Reconstruction
        current = dummy

        for val in stack:
            current.next = ListNode(val=val)
            current = current.next

        return dummy.next

        """
        Step 4: Optimize and Improve
        - Time Complexity: O(n), where n is the number of nodes in the linked list.
        - Space Complexity: O(n), due to use of the stack and new list construction.

        Step 5: Follow-Up Questions to Deepen Understanding
        1. How would this change if we wanted to remove nodes with smaller values to the right instead?
        2. Could we perform this in-place without additional space for a stack?
        3. What happens if the list is sorted in descending order?
        4. Can we generalize this pattern to solve similar problems involving comparisons across nodes?

        Patterns to Take to Future Problems:
        - Monotonic Stack: Used for filtering elements based on future comparisons (e.g., Next Greater Element).
        - Linked List Reconstruction: Build a new structure after logical filtering using dummy nodes.
        - Greedy Elimination: Proactively remove elements that won’t contribute to the optimal result.
        """
