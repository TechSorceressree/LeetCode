class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        slist = set(nums)
        if len(nums) == len(slist):
            return False
        return True
        