'''

Why can you print individual elemements 
  in a python string?

What amazes me is 

  why did they use a dictionary for
    key value access of opening and 
    corresponding parenthesis

  Why is a dictionary unordered?
    In dictionary we loop through the keys

  8.3 in EPI

'''
#-----------------------------------------
# Style 1
# What important thing did you learn from this style
#   that will help your problem solving skills moving forward

def is_well_formed(s):

  open_symb_store = []

  lookup_table = {'(':')', '{':'}', '[':']'}

  #Loop through each symbol entered
  for symbol in s:
    # if symbol is an open parenthesis, since we loop through the keys in a dictionary
    if symbol in lookup_table:

      #Store the open parentheis
      open_symb_store.append(symbol)

    # A not statement means the false condition evaluates to true
    # In our case, if we have an empty open symbol store (edge case)
    # This works for inputs such as "))))))"
    elif not open_symb_store:
      return False 

    # Based on our open symbol store
    # We check if the recently added open symbolto our store has a matching closing symbol
    # This is where the stack comes in
    # Now incases of nested opening parenthesis (edge case)
    #   The corresponding closing symbol will be based on the last inserted parenthesis
    elif lookup_table[open_symb_store.pop()] != symbol:
      return False
    
  
  
  # In cases where we have an empty string (edge case)
  #   A nice question will be what should we return when we have an empty input?
  # We return True statement, meaning we have a valid parentheis
  return not open_symb_Store

'''
Time complexity: O(n)

Learn how to calculate space complexity
Space Complexity: O(n)
'''
#-------------------------------------------------


