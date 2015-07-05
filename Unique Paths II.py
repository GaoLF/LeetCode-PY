class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        height = len(obstacleGrid)
        if not height:
            return 0
        width = len(obstacleGrid[0])
        left = up = 0
        for i in range(height):
            for j in range(width):
                if not i and not j:
                    if obstacleGrid[i][j]:
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = 1
                elif obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                else:
                    if i > 0:
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]
                    if j > 0:
                        obstacleGrid[i][j] += obstacleGrid[i][j-1]
        return obstacleGrid[height-1][width-1]



A = Solution()
print A.uniquePathsWithObstacles([])
print A.uniquePathsWithObstacles([[1]])
print A.uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]])