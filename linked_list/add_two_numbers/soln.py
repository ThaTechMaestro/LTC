'''
Question:
    https://leetcode.com/problems/add-two-numbers/?envType=problem-list-v2&envId=recursion
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
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
        
        

'''
ITERATIVE SOLUTION
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        
        Step 1: Identify Key Concepts Needed
        - Linked List Traversal: Iterate through the lists node by node.
        - Digit-wise Addition with Carry Handling: Perform addition like manual sum.
        - Handling Different Lengths: If one list is shorter, continue with the longer one.
        - Creating a New Linked List: Construct the sum in a new linked list.
        - Recursion: Implement a recursive approach to solve the problem.

        Step 2: Break Down the Solution Approach
        - Use a helper function `addNodes` to recursively process both linked lists while handling carry.
        - Sum the values at each node and propagate the carry.
        - Construct a new node for each sum result and recursively process the remaining nodes.
        
        Step 3: Implement the Code
        """
        
        def addNodes(l1: ListNode, l2: ListNode, carry: int) -> ListNode:
            """Helper recursive function to add nodes from l1 and l2 with carry."""
            if not l1 and not l2 and not carry:
                return None
            
            # Calculate new value and new carry
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            new_carry = total // 10
            new_val = total % 10
            
            # Create new node with the current digit and recurse for the next digits
            new_node = ListNode(new_val)
            new_node.next = addNodes(l1, l2, new_carry)
            return new_node
        
        # Initial call to the recursive function with carry 0
        return addNodes(l1, l2, 0)
        
        """
        Step 4: Optimize and Improve
        - Time Complexity: O(max(N, M)) where N, M are lengths of l1 and l2.
        - Space Complexity: O(max(N, M)) due to recursion depth.
        
        Step 5: Follow-Up Questions to Deepen Understanding
        1. How would the solution change if the numbers were stored in forward order?
        2. How does the recursive approach compare to an iterative approach in terms of space usage?
        3. What if we had doubly linked lists instead of singly linked lists?
        4. How would memory constraints impact this approach for large inputs?
        """
