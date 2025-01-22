class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #Automatically assigns a default value to any key that does not exist in the dictionary

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)          #Using immutable alternatives to represent list-like data as keys as Lists cannot be dictionary keys because they are mutable and not hashable

        return list(result.values())    #return list of the values of the dictionar E.g: ["eat","tea","tan","ate","nat","bat"]. Also, the function (-> List[List[str]]) expects Lists of list of strings to be returned 