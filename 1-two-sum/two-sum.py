class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevValMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevValMap:
                return [prevValMap[diff], i]
            prevValMap[n] = i
        