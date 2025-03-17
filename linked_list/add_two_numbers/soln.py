'''
Question:
    https://leetcode.com/problems/add-two-numbers/?envType=problem-list-v2&envId=recursion
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Problem: Add Two Numbers (LeetCode 2)
        Given two non-empty linked lists representing two non-negative integers, where digits are stored in
        reverse order, add the two numbers and return the sum as a linked list.

        Step 1: Identify Key Concepts Needed
        - Linked List Traversal: Iterate through the lists node by node.
        - Digit-wise Addition with Carry Handling: Perform addition like manual sum.
        - Handling Different Lengths: If one list is shorter, continue with the longer one.
        - Creating a New Linked List: Construct the sum in a new linked list.

        Step 2: Break Down the Solution Approach
        - Use a dummy node (`start`) to track the head of the result list.
        - Traverse both linked lists while carrying over extra sum if necessary.
        - Append new nodes with the sum of corresponding digits.
        - If a carry remains after processing all nodes, add an extra node.

        Step 3: Implement the Code
        """
        
        '''
        ITERATIVE SOLUTION
        '''
        start = ListNode()  # Dummy node to track result list
        curr = start  # Pointer to build the new linked list
        carry_over = 0  # Carry for digit-wise addition
        
        # Step 2: Traverse both lists until both are exhausted, considering carry
        while l1 or l2 or carry_over:
            total = carry_over 
            
            if l1:
                total += l1.val
                l1 = l1.next
            
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry_over = total // 10  # Compute carry for next iteration
            curr.next = ListNode(total % 10)  # Store current digit in new node
            curr = curr.next  # Move to next node in result list
        
        return start.next  # Return the actual head of the result list
        
        """
        Step 4: Optimize and Improve
        - Time Complexity: O(max(N, M)) where N, M are lengths of l1 and l2.
        - Space Complexity: O(max(N, M)) for the new linked list.
        
        Step 5: Follow-Up Questions to Deepen Understanding
        1. How would the solution change if the numbers were stored in forward order?
        2. Can this be solved recursively instead of iteratively? [DONE]
        3. What if we had doubly linked lists instead of singly linked lists?
        4. How would memory constraints impact this approach for large inputs?
        """