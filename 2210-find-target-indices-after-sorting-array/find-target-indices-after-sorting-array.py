class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        lis=[]
        for i in range(len(nums)):
            if nums[i]==target:
                lis.append(i)
        return lis

        