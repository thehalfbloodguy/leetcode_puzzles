# https://leetcode.com/problems/permutation-sequence/

from itertools import permutations
from math import factorial


class NaiveSolution:
    def getPermutation(self, n: int, k: int) -> str:
        perm_generator = permutations(range(1, n + 1))
        result = map(str, list(perm_generator)[k-1])
        return "".join(list(result))


class EfficientSolution:
    # much faster & memory efficient
    def getFirstIndex(self, n: int, k: int) -> (int, int):
        if n == 1:
            return 0, k
        fn = factorial(n - 1)
        index = k // fn
        new_k = k % fn
        return index, new_k

    def getPermutation(self, n: int, k: int) -> str:
        k -= 1

        digits_set = set()
        for el in range(1, n + 1):
            digits_set.add(el)
        remaining_list = list(digits_set)

        result = []
        while k > 0:
            index, k = self.getFirstIndex(n, k)
            next_digit = remaining_list.pop(index)
            result.append(next_digit)
            n -= 1
        result += remaining_list
        return "".join(list(map(str, result)))