#coding=utf-8
class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        # 我是通过把v1 和v2变成两个列表进行比较的
        # 方法固然比较复杂，但是好在一遍ac了
        l1 = []
        l2 = []
        v1 = version1 + '.'
        v2 = version2 + '.'
        i = j = 0
        while j < len(v1):
            if v1[j:j+1] == '.':
                if j == i :
                    l1.append(0)
                else:
                    l1.append(int(v1[i:j]))
                j += 1
                i = j
            else:
                j += 1
        i = j = 0
        while j < len(v2):
            if v2[j:j+1] == '.':
                if j == i :
                    l2.append(0)
                else:
                    l2.append(int(v2[i:j]))
                j += 1
                i = j
            else:
                j += 1
        for i in range(len(l1)-1,-1,-1):
            if not l1[i]:
                del(l1[i])
            else:
                break
        for i in range(len(l2)-1,-1,-1):
            if not l2[i]:
                del(l2[i])
            else:
                break
        for i in range(len(l1)):
            if i < len(l2):
                if l1[i] < l2[i]:
                    return -1
                elif l1[i] > l2[i]:
                    return 1
            else:
                return 1
        if l1 == l2:
            return 0
        else:
            return -1

A = Solution()
print A.compareVersion('1.2.3.4.5','1.2.3.4')
print A.compareVersion('1.2.3.4.5','')
print A.compareVersion('3.2.3.4.5','1.3.4')
