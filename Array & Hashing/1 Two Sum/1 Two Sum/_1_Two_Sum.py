class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pos = {}
        for index, value in enumerate(nums) :
            if (target - value) in pos :
                return [pos[target - value], index]
            pos[value] = index
        return []
print(Solution().twoSum([3,4,5,6], 7))
