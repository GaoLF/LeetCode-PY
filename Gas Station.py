class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        size = len(gas)
        begin = 0
        flag = 1
        while flag and begin < size:
            tank = gas[begin]
            if tank < cost[begin]:
                begin += 1
                continue
            tank -= cost[begin]
            i = begin + 1
            if i == size:
                flag = 0
                i = 0
            while i != begin:
                tank += gas[i]
                if tank < cost[i]:
                    break
                tank -= cost[i]
                i += 1
                if i == size:
                    flag = 0
                    i = 0
            else:
                return begin
            begin = i
        return -1

A = Solution()
print A.canCompleteCircuit([2,3],[3,2])


