import sys
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        len_row = len(grid)
        if not len_row:
            return 0
        len_col = len(grid[0])
        if not len_col:
            return 0
        flag = [[0 for i in range(0,len_col)] for i in range(0,len_row)]
        #print flag
        for i in range(0,len_row):
            for j in range(0,len_col):
                if not i and not j:
                    flag[i][j] = grid[i][j]
                else:
                    from_up = from_left = sys.maxint
                    if i>0:
                        from_up = flag[i-1][j]
                    if j>0:
                        from_left = flag[i][j-1]
                    flag[i][j] = min(from_up,from_left) + grid[i][j]
        return flag[len_row-1][len_col-1]


A = Solution()
print A.minPathSum([[1,2],[2,4],[4,5]])