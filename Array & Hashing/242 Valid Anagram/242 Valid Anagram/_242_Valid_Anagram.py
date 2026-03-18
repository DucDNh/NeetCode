class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        amount_s = {}
        for c in s :
            if c in amount_s :
                amount_s[c] += 1
            else :
                amount_s[c] = 1
        amount_t = {}
        for c in t :
            if c in amount_t :
                amount_t[c] += 1
            else :
                amount_t[c] = 1
        for c in amount_s.keys() :
            if amount_s.get(c, 0) != amount_t.get(c, 0) :
                return False
        return True
print(Solution().isAnagram("racecar", "carrace"))