class Solution:
    def encode(self, strs: List[str]) -> str:
        encdstr=""
        for s in strs:
            encdstr+=str(len(s))+"#"+s
        return encdstr
     
    def decode(self, s: str) -> List[str]:
        decdstr, i = [], 0

        while i<len(s):
            j = i
            
            while s[j]!="#":
                j+=1
            length=int(s[i:j])

            decdstr.append(s[j+1:j+1+length])

            i=j+1+length

        return decdstr
