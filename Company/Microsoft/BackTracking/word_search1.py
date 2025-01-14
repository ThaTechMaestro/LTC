
'''
Helpful Links:
    https://leetcode.com/problems/word-search/discuss/1538495/Python-solution-using-backtracking-with-explanation
    Neetcode:- Word Search Problem Solution

A set is:
  an unordered collection
  It prevents duplicates
  It is implemented under the hood as hash map
    using the values inserted in the set as key.
  Set(1,2,3,4) -> {'1':None, '2':None, '3':None, '4':None}

  Quick look up time

'''

class Solution:

  '''
  The algorithm:
  
    Check if all the characters in the given word exists
      in the characters that make up the board
        return 

    
  
  '''

  def get_word_search_status(self, board, word):

    '''
    Defined a data structure to store all the character in our board
    We chose a set for:
      Quick lookup time
      
    '''
    board_characters = set()


    for row in board:
      for column_value in row:
        if column_value not in board_characters:
          board_characters.add(column_value)

    


    '''
    We are peforming lookup, hence why we chose a set 
    which has O(1) lookup time
    Optimisation1
    
    '''        
    for character in word:
      if character not in board_characters:
        return False

        

    ROWS, COLS = len(board), len(board[0])
    '''
    What I understand of the algorithm:
      You take a character at a particular index in the BOARD
        compare it with a character gotten from a particular index of the given WORD

      if it is false:

      if it is true:
        You add the character to the visited path
        you move on to the next word (but in what direction, up, down, left)
        Increment the index used to access a character of the given WORD
    
    '''
    def depth_first_search(row_index, col_index, word_index, visited_path):

      '''
      First check occurs due to recursive stack
      The valid index check
      '''
      if row_index < 0 or row_index > len(board) - 1 or col_index < 0 or col_index > len(board[0]) - 1: 
        return False


      '''
      Second Check
        if board_character have been visited in the past
      '''
      if (row_index, col_index) in visited_path:
        return False 


      
      '''
      The actual algorithm clause
      OPTIMISATION 3
        Only perform valid word character check and depth first search
            if the character at the index from the BOARD
            matches the character at the current index from the given WORD 
      '''
      if board[row_index][col_index] == word[word_index]:
        visited_path.add((row_index, col_index))

        #Valid recursive condition breaker
        if word_index == len(word)-1:
          return True 
        
        # recursive Depth first search
        word_search_status = (depth_first_search(row_index, col_index+1, word_index+1, visited_path) or
                              depth_first_search(row_index, col_index-1, word_index+1, visited_path) or
                              depth_first_search(row_index+1, col_index, word_index+1, visited_path) or
                              depth_first_search(row_index-1, col_index, word_index+1, visited_path))

        
        #This part is confusing
        visited_path.remove((row_index, col_index))
        return word_search_status

      return False

        

  
      
    #Engine Section
    for row_index in range(ROWS):
      for column_index in range(COLS):

        '''
        If a character at particular index in the BOARD 
        is the same as a character at the first index in of the given WORD, 
        that is only when we perform the dfs

        There is no point performing a dfs 
        starting with an invalid character

        It is a great optimisation
        OPTIMISIATION 2

        This is the engine section of our program
          This is where our program gets executed
        '''
           

        if (board[row_index][column_index] == word[0]):
          visited_path = set()

          if depth_first_search(row_index, column_index, 0, visited_path):
            return True

    
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
a = Solution()
print(a.get_word_search_status(board, word))



        
