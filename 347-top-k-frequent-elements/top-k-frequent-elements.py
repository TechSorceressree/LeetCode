class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}

        for num in nums:
            freqmap[num] = 1 + freqmap.get(num, 0)
        
        arr = []
        for num, cnt in freqmap.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while(len(res)<k):
            res.append(arr.pop()[1])
        return res