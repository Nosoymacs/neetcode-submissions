class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = set(nums)
        if len(copy) != len(nums):
            return True
        return False