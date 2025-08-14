class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = Counter(nums)
        return heapq.nlargest(k, freqmap.keys(), key=freqmap.get)