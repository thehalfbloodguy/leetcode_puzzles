# https://leetcode.com/problems/4sum/

from typing import List


class Solution(object):
    def fourSum(self, nums: List[int], target: int):
        sorted_nums = sorted(nums)
        length = len(nums)
        ab_pairs = {}
        for a in range(length - 3):
            for b in range(a + 1, length - 2):
                ab_sum = sorted_nums[a] + sorted_nums[b]
                try:
                    ab_pairs[target - ab_sum].append([a, b])
                except KeyError:
                    ab_pairs[target - ab_sum] = [[a, b]]
        results = set()
        for residual_sum, temp in ab_pairs.items():
            for pair in temp:
                a = pair[0]
                b = pair[1]
                c = pair[1]+ 1
                d = length - 1
                while c < d:
                    # 2 pointers: c, d
                    cd_sum = sorted_nums[c] + sorted_nums[d]
                    if cd_sum == residual_sum:
                        solution = (sorted_nums[a], sorted_nums[b], sorted_nums[c], sorted_nums[d])
                        results.add(solution)
                        c += 1
                    elif cd_sum < residual_sum:
                        c += 1
                    else:
                        d -= 1
        return results