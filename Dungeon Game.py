class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    # 果然一个题如果没有亲子写就会有很多问题，C++的没有亲子写
    # 这个题目从后边往前边找，hp数组存的是当前点最小的血量
    # 周围padding一下，只把d[i][j]的右边点和下边点设为1，其他的行列设置为INT_MAX
    # 使得可以少很多判断条件
    # 当前点的血量计算方法是：下边一个点或右边一个点的血量的较小值减去当前可能受到的伤害
    # 如果结果小于0，说明当前点不需要特别留血，只需要保持1点即可
    # 如果结果大于0，说明当前点需要留血，留着这个正数
    # 至于为什么要用减法：因为当前点的血量 = 上边或左边的血量 + 当前的加血或减血
    # 因为是倒着做的，上边或左边的血量 = 右边或下边的血量 - 加血或扣血
    def calculateMinimumHP(self, dungeon):
        rows = len(dungeon)
        if not rows:
            return 1
        cols = len(dungeon[0])
        if not cols:
            return 1
        hp = [[1<<30 for i in xrange(cols+1)]for j in xrange(rows+1)]
        hp[rows-1][cols] = hp[rows][cols-1] = 1
        for i in xrange(rows-1,-1,-1):
            for j in xrange(cols-1,-1,-1):
                need = min(hp[i+1][j],hp[i][j+1])-dungeon[i][j]
                if need <= 0:
                    need = 1
                hp[i][j] = need
        return hp[0][0]




A = Solution()
print A.calculateMinimumHP([[-3],[-7]])
print A.calculateMinimumHP([[1,-4,5,-99],[2,-2,-2,-1]])
print A.calculateMinimumHP([[-2,-3,3],[-5,10,1],[10,30,-5]])