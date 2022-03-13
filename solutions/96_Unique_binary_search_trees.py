# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:

    def __init__(self):
        self.numTrees = {0: 1, 1: 1}

    def getNumTrees(self, n: int) -> int:
        if n in self.numTrees:
            return self.numTrees[n]
        else:
            result = 0
            for right_size in range(0, n):
                result += self.getNumTrees(right_size) * self.getNumTrees(n - 1 - right_size)
            self.numTrees[n] = result
            return result