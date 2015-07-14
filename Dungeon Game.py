class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    # ��Ȼһ�������û������д�ͻ��кܶ����⣬C++��û������д
    # �����Ŀ�Ӻ����ǰ���ң�hp�������ǵ�ǰ����С��Ѫ��
    # ��Χpaddingһ�£�ֻ��d[i][j]���ұߵ���±ߵ���Ϊ1����������������ΪINT_MAX
    # ʹ�ÿ����ٺܶ��ж�����
    # ��ǰ���Ѫ�����㷽���ǣ��±�һ������ұ�һ�����Ѫ���Ľ�Сֵ��ȥ��ǰ�����ܵ����˺�
    # ������С��0��˵����ǰ�㲻��Ҫ�ر���Ѫ��ֻ��Ҫ����1�㼴��
    # ����������0��˵����ǰ����Ҫ��Ѫ�������������
    # ����ΪʲôҪ�ü�������Ϊ��ǰ���Ѫ�� = �ϱ߻���ߵ�Ѫ�� + ��ǰ�ļ�Ѫ���Ѫ
    # ��Ϊ�ǵ������ģ��ϱ߻���ߵ�Ѫ�� = �ұ߻��±ߵ�Ѫ�� - ��Ѫ���Ѫ
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