'''
Question
    https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/?envType=problem-list-v2&envId=recursion
Core Concepts: 
- Recursive Problem Solving: Think of this problem as a repetitive process where each step builds upon the previous result.
- Sequence Expansion: Visualize the sequence growing like layers being added to a structure, one step at a time.
- Modular Arithmetic for Wrapping: When counting in cycles (like 'a' to 'z' then back to 'a'), use modulo operations.
- Base and Recursive Cases: Always define a clear stopping condition (base case) and a consistent way to move towards it (recursive step).

Solution Approach: 
- Start with the smallest sequence ('a' as [0]) and recursively generate the next sequence by incrementing each character.
- Using the chr function to get the int to character equivalent
- Stop recursion once the sequence length meets or exceeds k, then directly fetch the k-th character.

Time Complexity: O(k) - The sequence generation continues until at least k elements are reached.
Space Complexity: O(k) - Additional memory is used for the recursive call stack and the growing sequence.
Optimality: This solution is optimal as it generates the minimal necessary sequence and leverages recursion to avoid unnecessary iterations.

'''

class Solution:
    '''
    Something interesting this recursive call
        has no extra logic after base call logic and input data logic
        so it just retruns what ever the base returns as
        the method calls in the stack completes
    '''
    def kthCharacter(self, k: int) -> str:
        def generate_sequence(v):
            # Base case: If the length of the sequence is at least k, return the k-th character
            if len(v) >= k:
                return chr(v[k-1] + 97)  # Convert index to corresponding character
            
            # Generate the next sequence recursively
            next_sequence = [((char + 1) % 26) for char in v]
            
            # Call the recursive function with the expanded sequence
            return generate_sequence(v + next_sequence)
        
        # Start with the initial list representing 'a'
        return generate_sequence([0])


