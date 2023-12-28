class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        lenS, lenT = len(s), len(t)

        for i in range(lenT, 0, -1):
            if lenS % i == 0 and lenT % i == 0:  
                cur = s[:i]  
                if cur * (lenS // i) == s and cur * (lenT // i) == t:  
                    return cur

        return ''
                
                
        
        