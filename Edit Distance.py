# coding=utf-8
class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    """
    Use f[i][j] to represent the shortest edit distance between word1[0,i) and word2[0, j). Then compare the last character of word1[0,i) and word2[0,j), which are c and d respectively (c == word1[i-1], d == word2[j-1]):

if c == d, then : f[i][j] = f[i-1][j-1]

Otherwise we can use three operations to convert word1 to word2:

(a) if we replaced c with d: f[i][j] = f[i-1][j-1] + 1;

(b) if we added d after c: f[i][j] = f[i][j-1] + 1;

(c) if we deleted c: f[i][j] = f[i-1][j] + 1;

Note that f[i][j] only depends on f[i-1][j-1], f[i-1][j] and f[i][j-1], therefore we can reduce the space to O(n) by using only the (i-1)th array and previous updated element(f[i][j-1]).

 int minDistance(string word1, string word2) {

        int l1 = word1.size();
        int l2 = word2.size();

        vector<int> f(l2+1, 0);
        for (int j = 1; j <= l2; ++j)
            f[j] = j;

        for (int i = 1; i <= l1; ++i)
        {
            int prev = i;
            for (int j = 1; j <= l2; ++j)
            {
                int cur;
                if (word1[i-1] == word2[j-1]) {
                    cur = f[j-1];
                } else {
                    cur = min(min(f[j-1], prev), f[j]) + 1;
                }

                f[j-1] = prev;
                prev = cur;
            }
            f[l2] = prev;
        }
        return f[l2];

    }
   Actually at first glance I thought this question was similar to Word Ladder and \
   I tried to solve it using BFS(pretty stupid huh?). But in fact, the main difference is that\
   there's a strict restriction on the intermediate words in Word Ladder problem, while\
   there's no restriction in this problem. If we added some restriction on intermediate \
   words for this question, I don't think this DP solution would still work.
    """
    #这个题的方法参照与一个别人的方法，但是他是进一步用一维数组简化了该二维数组
    #总的来说，还是一个基于两个数组的dp算法
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        flag = [[0 for i in range(len2+1)]for i in range(len1+1)]
        for i in range(len1+1):
            flag[i][0] = i
        for j in range(len2+1):
            flag[0][j] = j
        for i in range(len1):
            for j in range(len2):
                if word1[i] == word2[j]:
                    flag[i+1][j+1] = flag[i][j]
                else:
                    flag[i+1][j+1]= min(flag[i][j],flag[i][j+1],flag[i+1][j])+1
        return flag[len1][len2]

A = Solution()
print A.minDistance("abc","bca")
print A.minDistance("a","abcd")
