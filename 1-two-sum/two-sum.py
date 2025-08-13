class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        vistedVals = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in vistedVals:
                return [vistedVals[diff], i]
            vistedVals[n] = i