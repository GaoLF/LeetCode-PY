class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])
        res = 0
        for i in xrange(rows):
            for j in xrange(cols):
                if grid[i][j] == '1':
                    res += 1
                    self.write_flag(grid,i,j)
        return res

    def write_flag(self,grid,i,j):
        if grid[i][j] != '1':
            return
        grid[i][j] = 'X'
        if i > 0 :
            self.write_flag(grid,i-1,j)
        if i + 1 < len(grid):
            self.write_flag(grid,i+1,j)
        if j > 0:
            self.write_flag(grid,i,j-1)
        if j + 1 < len(grid[0]):
            self.write_flag(grid,i,j+1)

A = Solution()
print A.numIslands([['1','1','0','0','0'],
                    ['1','1','0','0','0'],
                    ['0','0','1','0','0'],
                    ['0','0','0','1','1']])