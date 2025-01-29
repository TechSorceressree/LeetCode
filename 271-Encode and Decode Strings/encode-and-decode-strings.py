class Solution:
    def encode(self, strs: List[str]) -> str:
        enstr = ""

        for s in strs:
            enstr = str(len(s)) + "#" + s
        return enstr
         
    def decode(self, s: str) -> List[str]:
        destr, i = [], 0

        while i < len(s):

            j = i
            while s[j] !='#':
                j += 1
            length = int(s[i:j])
            destr.append(s[j + 1:j+1+length])
            i=j+1+length

        return destr