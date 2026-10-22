from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        res = float('inf')
        target = list(range(n))
        k = nums.index(0)
        if nums[k:] + nums[:k] == target:
            res = min(res, k, n - k + 2)
        rev_nums = nums[::-1]
        k_rev = rev_nums.index(0)
        if rev_nums[k_rev:] + rev_nums[:k_rev] == target:
            res = min(res, k_rev + 1, n - k_rev + 1)
        if res == float('inf'):
            return -1
        
        return int(res)