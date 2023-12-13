"""
Problem statement: 

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements 
in row i and column j are 0 (rows and columns are 0-indexed).


Approach: 

For this solution, I'll go through all the columns. For each column, I'll go through all the rows,
trying to determine if there is only one "1" in that column. If this is true, I'll raise a flag
that there is only one "1" in that column. While checking the rows, if I notice that the flag had
been raised earlier, I'll just stop checking the rows in that column because I know that column is
now invalid as it has more than one "1" in it

At the end of checking, if the flag is raised, I'll check this special row, to make sure that there's
no other "1" in the special row, apart from the one in the column I'm currently at. If so, I update
the count. If not, I move on to the next column.
"""
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        height = len(mat)
        width = len(mat[0])

        count = 0

        for c_ind in range(width):
            special_row_ind = None

            for r_ind in range(height):
                if mat[r_ind][c_ind] == 1:
                    if special_row_ind is not None:
                        break
                    special_row_ind = r_ind


            if special_row_ind is not None:
                if 1 not in mat[special_row_ind][:c_ind] + mat[special_row_ind][c_ind+1:]:
                    count += 1

            return count


soln = Solution()
mat = [
    [1, 0, 0],
    [0, 0, 1],
    [1, 0, 0]
]
print(soln.numSpecial(mat))