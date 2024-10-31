'''
Question
https://www.designgurus.io/course-play/grokking-data-structures-for-coding-interviews/doc/problem-3-row-with-maximum-oneseasy


'''

class Solution:
    def findMaxOnesRow(self, mat):
        maxOnesIdx, maxOnesCount = 0, 0  # Initialize tracking variables
        # ToDo: Write Your Code Here.

        for i in range(len(mat)):

            if mat[i].count(1) > maxOnesCount:
                maxOnesCount = mat[i].count(1)
                maxOnesIdx = i

        return [maxOnesIdx, maxOnesCount]  