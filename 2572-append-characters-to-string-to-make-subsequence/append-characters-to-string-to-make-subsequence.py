class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0

        for ch in s:
            if ch == t[j]:
                j += 1

                if j == len(t):
                    return 0
        
        return len(t) - j