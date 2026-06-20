class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            n = str(len(word))
            res += n + "$" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            n = ""
            while j < len(s):
                if s[j].isdecimal():
                    n += s[j]
                else:
                    break
                j += 1
            n = int(n)
            
            start = j + 1
            end = start + n
            word = s[start:end]
            res.append(word)
            i = end
        
        return res


