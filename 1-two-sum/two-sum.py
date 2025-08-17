class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valSet = {}

        for i, n in enumerate(nums):
            diff = target - n
            if(diff in valSet):
                return [valSet[diff], i]
            valSet[n] = i     