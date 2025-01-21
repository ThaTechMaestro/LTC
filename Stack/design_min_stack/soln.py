'''
Question:
https://leetcode.com/problems/min-stack/description/
'''

class MinStack:
    def __init__(self):
        # Main stack to store all values
        self.storage = []
        # Auxiliary stack to store minimum values
        self.min_storage = []

    def push(self, val):
        """
        Push value onto the stack.
        Also push to min_storage if it's the smallest value so far.
        Time Complexity: O(1)
        
        The "val <= self.min_storage[-1]" covers a very unqiue scenario
        of if there are duplicate minimum in the stack and only one
        was popped from the stack
        """
        self.storage.append(val)
        if not self.min_storage or val <= self.min_storage[-1]:
            self.min_storage.append(val)

    def pop(self):
        """
        Remove the top value from the stack.
        If it's the current minimum, also remove it from min_storage.
        Time Complexity: O(1)
        """
        if self.storage:
            val = self.storage.pop()
            if val == self.min_storage[-1]:
                self.min_storage.pop()

    def top(self):
        """
        Get the top value of the stack.
        Time Complexity: O(1)
        """
        if not self.storage:
            return None
        return self.storage[-1]

    def getMin(self):
        """
        Retrieve the current minimum value.
        Time Complexity: O(1)
        """
        if not self.min_storage: return None
        return self.min_storage[-1]
