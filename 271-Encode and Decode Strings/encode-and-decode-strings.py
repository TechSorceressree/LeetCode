class Solution:
    def encode(self, strs: List[str]) -> str:
        encstr=""
        for s in strs:
            encstr+=str(len(s))+"#"+s
        return encstr
     
    def decode(self, s: str) -> List[str]:
        decstr, i = [], 0

        while i<len(s):
            j = i
            
            while s[j]!="#":
                j+=1
            length=int(s[i:j])

            decstr.append(s[j+1:j+1+length])

            i=j+1+length

        return decstr
