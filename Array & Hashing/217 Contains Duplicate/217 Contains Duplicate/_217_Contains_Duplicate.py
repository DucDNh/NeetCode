class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        num_seen = set()
        for num in nums :
            if num in num_seen :
                return True
            else :
                num_seen.add(num)
        return False 

test_nums = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 1]
print(Solution().hasDuplicate(test_nums))


